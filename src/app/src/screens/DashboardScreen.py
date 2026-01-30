from textual import work
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Label, Button, ProgressBar, Static
from textual.containers import Vertical, Center, Horizontal, Container
from pathlib import Path
from ..utils.typo import Profile
from ..utils.fileHandling import checkPathExists, removeDir
from ..mclib.mclib import install_mc, execute_mc
from ..styles.Styles import Styles
import asyncio

class Dashboard(Screen):
    
    CSS = Styles.dashboardScreen
    
    def __init__(self, profile: Profile, name: str | None = None, id: str = None, classes: str = None):
        self.profile = profile
        self.info_static = f"Bienvenido {self.profile.username}\nVersion seleccionada {self.profile.version}. API: {self.profile.api}"
        super().__init__(name, id, classes)
    
    def compose(self) -> ComposeResult:
        yield Container(
            Static(self.info_static, classes="info_static"),
            Center(ProgressBar(total=100, show_eta=False, id="download_pb")),
            Horizontal(
                Button(label="Instalar", id="install_btn", classes="button"),
                Button(label="Jugar", id="play_btn", classes="button", disabled=True),
                classes="buttons"
            ),
            id="dashboard"
        )

    async def on_mount(self):
        minecraftPathExists = await asyncio.to_thread(checkPathExists, Path(self.profile.minecraftPath))
        
        if minecraftPathExists:
            playButton = self.query_one("#play_btn", Button)
            playButton.disabled = False
            
            installButton = self.query_one("#install_btn", Button)
            installButton.disabled = True
            installButton.label = "Instalado"
            
            verticalForPb = self.query_one("#progress_container", Vertical)
            verticalForPb.add_class("hidden")
            
    async def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "install_btn":
            event.button.disabled = True
            event.button.label = "Instalando..."
            self.installMinecraft()
            
        elif event.button.id == "play_btn":
            self.executeMinecraft()
    
    @work(exclusive=True, thread=True)
    def installMinecraft(self):
        installButton = self.query_one("#install_btn", Button)
        playButton = self.query_one("#play_btn", Button)
        progressBar = self.query_one("#download_pb", ProgressBar)
        
        def set_max(new_max: int):
            self.app.call_from_thread(lambda: setattr(progressBar, "total", new_max))
        
        def set_progress(progress: int):
            self.app.call_from_thread(lambda: setattr(progressBar, "progress", progress))
        
        callback = {
            "setProgress": set_progress,
            "setMax": set_max
        }

        try:
            self.notify(f"Iniciando Instalacion de Minecraft v{self.profile.version}", severity="information")
            
            install_mc(
                version=self.profile.version,
                path=Path(self.profile.minecraftPath),
                callback=callback
            )
            
            def onSuccessEnableButton():
                progressBar.show_bar = False
                playButton.disabled = False
                self.notify(f"🎮 ¡Minecraft {self.profile.version} listo para jugar!", 
                            severity="success",
                            timeout=8)
            
            self.app.call_from_thread(onSuccessEnableButton)
        
        except Exception as e:
            def showError():
                installButton.disabled = False
                removeDir(Path(self.profile.minecraftPath))
                self.notify(f"Error: {str(e)}", severity="error")
            
            self.app.call_from_thread(showError)
                
        
    @work(exclusive=True, thread=True)
    def executeMinecraft(self):
        try:
            execute_mc(
                    username=self.profile.username,
                    mcVersion=self.profile.version,
                    mcPath=self.profile.minecraftPath
            )
            self.notify(f"Ejecutando Minecraft v{self.profile.version}")
        
            self.app.call_from_thread(
                lambda: self.notify("Minecraft cerrado", severity="information")
            )
            
        except Exception as e:
            self.notify("Error al iniciar minecraft", severity="error")