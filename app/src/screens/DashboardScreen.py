from textual import work
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Label, Button
from pathlib import Path
from ..utils.typo import Profile
from ..mclib.mclib import install_mc, execute_mc

class Dashboard(Screen):
    
    def __init__(self, profile: Profile, name: str | None = None, id: str = None, classes: str = None):
        self.profile = profile
        super().__init__(name, id, classes)
    
    def compose(self) -> ComposeResult:
        yield Label(f"Bienvenido {self.profile.username}", id="welcome_label")
        yield Label(f"Version seleccionada {self.profile.version}. API: {self.profile.api}")
        
        yield Button(label="Instalar",
                     id="install_btn")
        
        yield Button(label="Jugar",
                     id="play_btn")
    
    # @work
    # async def on_mount(self):
    #     playButton = self.query_one("#install_btn", Button)
        
        
    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "install_btn":
            install_mc(
                version=self.profile.version,
                path=Path(self.profile.minecraftPath)
            )
            
        elif event.button.id == "play_btn":
            execute_mc(
                username=self.profile.username,
                mcVersion=self.profile.version,
                mcPath=self.profile.minecraftPath
            )
    
    # def searchVersion(self):
    #     versionsJson = openJson()
        
    #     for version in versionsJson["versions"]:
    #         if version["id"] == self.profile.version and version["type"] == "release":
    #             return version

    # def on_mount(self):
    #     version = self.searchVersion()
        
    #     self.query_one("#welcome_label", Label).content = version["url"]