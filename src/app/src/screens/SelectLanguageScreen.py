from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Container, Horizontal
from textual.widgets import Button, Footer, Header, Static
from ..styles.Styles import Styles
from ..utils.miscFunctions import createLangFile

class SelectLanguage(Screen):
    
    CSS = Styles.language_styles
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Container(
            Static("Select One of the Following Languages\nSelecciona uno de los idiomas siguientes", classes="question"),
            Horizontal(
                Button("English", id="english_btn"),
                Button("Español", id="spanish_btn"),
                classes="buttons",
            ),
            id="dialog",
        )
        
    def on_button_pressed(self, event: Button.Pressed):
        from .ProfilesScreen import Profiles
        if event.button.id.startswith("english"):
            createLangFile(english=True)
            self.app.push_screen(Profiles())
        elif event.button.id.startswith("spanish"):
            createLangFile(spanish=True)
            self.app.push_screen(Profiles())
                