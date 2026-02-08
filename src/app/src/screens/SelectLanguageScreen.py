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
        
        if event.button.id.startswith("english"):
            createLangFile(english=True)
            self.notify(
                title="✅ Language Selected",
                message="Kaleido will close, please restart it",
                timeout=3
            )
            
        elif event.button.id.startswith("spanish"):
            createLangFile(spanish=True)
            self.notify(
                title="✅ Idioma Seleccionado",
                message="Kaleido se cerrará, por favor reinicielo",
                timeout=3
            )
        
        self.set_timer(3, self.app.exit)