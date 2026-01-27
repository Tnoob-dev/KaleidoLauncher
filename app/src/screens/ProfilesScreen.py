from textual.app import ComposeResult
from textual.screen import Screen
from textual.widget import Widget
from textual.widgets import Label, Button, Input, Footer, Header
from ..utils.fileHandling import checkConfigExists
from pathlib import Path

class ProfileCreation(Screen):
    def compose(self) -> ComposeResult:
        yield Header("Creacion de Perfil")
        yield Label("Introduce el nombre que nos acompañara en este gran viaje:")
        yield Input(placeholder="Steve", id="name_input")
        yield Button("Crear", id="create_btn", disabled=True)    
        yield Footer()
    
    def on_input_changed(self, event: Input.Changed) -> None:
        
        inputWidget = self.query_one("#name_input", Input)
        disabledButton = self.query_one("#create_btn", Button)
        
        disabledButton.disabled = len(inputWidget.value.strip()) < 4


class Profiles(Widget):
    
    def compose(self) -> ComposeResult:
        fileExists = checkConfigExists(Path("./profiles.json"))
        
        if not fileExists:
            yield Label("No existe archivo de configuracion", id="no-config-label")
            yield Button("Crear Nuevo Perfil", id="create_profile_btn")
            return

        yield Label("Selecciona un perfil")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "create_profile_btn":
            self.app.push_screen(ProfileCreation())
        