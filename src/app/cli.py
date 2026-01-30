from textual import work
from textual.app import App, ComposeResult
from textual.widgets import Header
from app.src.screens.ProfilesScreen import Profiles
from app.src.themes.themes import MyThemes
from app.src.utils.miscFunctions import createKaleidoFolder, whatPlatform
from app.src.styles.Styles import Styles
import asyncio

class Kaleido(App):
    ENABLE_COMMAND_PALETTE = False
    
    CSS = Styles.profileScreen
    
    BINDINGS = [("q, ctrl+c", "quit", "Cerrar"),
                ("1", "change_theme('minecraft')", "Tema de Minecraft"),
                ("2", "change_theme('nether')", "Tema de Nether"),
                ("3", "change_theme('end')", "Tema de End"),
                ]
    
    TITLE = "Kaleido - Launcher"
    
    
    def compose(self) -> ComposeResult:
        yield Header()
    
    @work
    async def on_mount(self) -> None:
        self.register_theme(MyThemes.minecraft_theme)
        self.register_theme(MyThemes.nether_theme)
        self.register_theme(MyThemes.end_theme)
        
        self.theme = "end"
        
        platformPath = whatPlatform()
        
        await asyncio.to_thread(createKaleidoFolder, platformPath)
        self.push_screen(Profiles())
        
    def action_change_theme(self, themeName: str) -> None:
        self.theme = themeName
        
def main():
    app = Kaleido()
    app.run()
    
if __name__ == "__main__":
    main()