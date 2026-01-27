from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Welcome, Label, Button, Static
from textual import events
from textual.screen import Screen
from src.screens.ProfilesScreen import Profiles


class MyApp(App):
    
    CSS_PATH = "./src/styles/ProfileScreen.tcss"
    BINDINGS = [("q, ctrl+c", "quit", "Cerrar")]
    TITLE = "Kaleido - Launcher"
    
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Profiles()
        yield Footer()
    
            
if __name__ == "__main__":
    app = MyApp()
    app.run()