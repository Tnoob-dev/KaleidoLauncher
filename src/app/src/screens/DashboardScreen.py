from textual import work
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, ProgressBar, Static, Header, Footer
from textual.containers import Center, Horizontal, Container
from minecraft_launcher_lib.types import CallbackDict
from pathlib import Path
from typing import Optional
from ..utils.typo import Profile
from ..utils.fileHandling import checkPathExists, removeDir
from ..utils.miscFunctions import getMinecraftVersion
from ..mclib.mclib import minecraftInstall, execute_mc
from ..profiles.profileManagement import deleteProfiles, updateVersion
from ..styles.Styles import Styles
from ..langs.Languages import Langs
from app.cli import lang
import asyncio

class Dashboard(Screen):

    CSS = Styles.dashboardScreen

    def __init__(self, profile: Profile, name: str | None = None, id: Optional[str] = None, classes: Optional[str] = None):
        self.profile = profile

        super().__init__(name, id, classes)

    def compose(self) -> ComposeResult:
        kl_ascii = """
\t\t██╗  ██╗██╗
\t\t██║ ██╔╝██║
\t\t█████╔╝ ██║
\t\t██╔═██╗ ██║
\t\t██║  ██╗███████╗
\t\t╚═╝  ╚═╝╚══════╝
"""
        welcome = Langs.langsDict["welcome"][lang].format(username=self.profile.username)
        versionSelected = Langs.langsDict["versionSelected"][lang].format(
            version=self.profile.version,
            api=self.profile.api,
            ascii_art=kl_ascii
        )
        minecraftInstallationPath = Langs.langsDict["minecraftInstallationPath"][lang].format(
            path=self.profile.minecraftPath
        )

        info_static = f"{welcome}\n\t{versionSelected}\n{minecraftInstallationPath}"

        yield Header()
        yield Footer()

        yield Container(
            Horizontal(
                Button(label=Langs.langsDict["goBackButton"][lang], id="go_back"),
                Button(label=Langs.langsDict["deleteProfileButton"][lang], id="delete_profile")
            ),
            Static(
                info_static,
                classes="info_static"
            ),
            Center(ProgressBar(total=100, show_eta=False, id="download_pb"), id="progress_container"),
            Horizontal(
                Button(label=Langs.langsDict["installButton"][lang], id="install_btn", classes="button"),
                Button(label=Langs.langsDict["playButton"][lang], id="play_btn", classes="button", disabled=True),
                classes="buttons"
            ),
            classes="dashboard"
        )
    
    async def on_mount(self):
        minecraftPathExists = await asyncio.to_thread(checkPathExists, Path(Path(self.profile.minecraftPath) / ".minecraft"))

        if minecraftPathExists:
            playButton = self.query_one("#play_btn", Button)
            playButton.disabled = False

            installButton = self.query_one("#install_btn", Button)
            installButton.disabled = True
            installButton.label = Langs.langsDict["installedStatus"][lang]

            CenterForPb = self.query_one("#progress_container", Center)
            CenterForPb.add_class("hidden")

    async def on_button_pressed(self, event: Button.Pressed):
        from .ProfilesScreen import Profiles

        match event.button.id:
            case "install_btn":
                event.button.disabled = True
                event.button.label = Langs.langsDict["installingStatus"][lang]
                self.installMinecraft()

            case "play_btn":
                self.executeMinecraft()

            case "go_back":
                self.app.push_screen(Profiles())

            case "delete_profile":
                removeDir(Path(self.profile.minecraftPath) / ".minecraft")
                deleteProfiles(self.profile.username)
                self.notify(Langs.langsDict["profileRemovedNotification"][lang], severity="information", timeout=2)
                self.app.push_screen(Profiles())



    @work(exclusive=True, thread=True)
    def installMinecraft(self):
        installButton = self.query_one("#install_btn", Button)
        playButton = self.query_one("#play_btn", Button)
        progressBar = self.query_one("#download_pb", ProgressBar)

        def set_max(new_max: int):
            self.app.call_from_thread(lambda: setattr(progressBar, "total", new_max))

        def set_progress(progress: int):
            self.app.call_from_thread(lambda: setattr(progressBar, "progress", progress))

        callback: CallbackDict = {
            "setProgress": set_progress,
            "setMax": set_max
        }

        try:
            self.notify(Langs.langsDict["startingInstallationStatus"][lang].format(version=self.profile.version, api=self.profile.api),
                        severity="information")

            minecraftInstall(
                api=self.profile.api,
                version=self.profile.version,
                mcPath=Path(self.profile.minecraftPath),
                callback=callback
            )
            
            version = getMinecraftVersion(self.profile.minecraftPath)
                
            if version != "vanilla":
                updateVersion(self.profile.username, version)
                self.profile.version = version

            def onSuccessEnableButton():
                progressBar.show_bar = False
                playButton.disabled = False
                self.notify(Langs.langsDict["readyToPlayNotification"][lang].format(version=self.profile.version),
                            severity='information',
                            timeout=8)

            self.app.call_from_thread(onSuccessEnableButton)
            
        except Exception as e:
            def showError():
                installButton.disabled = False
                removeDir(Path(self.profile.minecraftPath) / ".minecraft")

            self.app.call_from_thread(showError)
            self.notify(f"Error: {str(e)}", severity="error")


    @work(exclusive=True, thread=True)
    def executeMinecraft(self):
        try:
            self.notify(Langs.langsDict["executingStatus"][lang].format(version=self.profile.version),
                        severity="information")

            execute_mc(
                    username=self.profile.username,
                    mcVersion=self.profile.version,
                    mcPath=Path(self.profile.minecraftPath),
                    player_uuid=self.profile.uuid
            )

            self.app.call_from_thread(
                lambda: self.notify(Langs.langsDict["closedStatus"][lang],
                                    severity="information")
            )

        except Exception as e:
            self.notify(Langs.langsDict["errorOpening"][lang].format(e),
                        severity="error")
