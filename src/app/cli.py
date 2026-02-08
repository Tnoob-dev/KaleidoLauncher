from textual import work
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from app.src.screens.ProfilesScreen import Profiles
from app.src.screens.SelectLanguageScreen import SelectLanguage
from app.src.themes.themes import MyThemes
from app.src.db.dbCreation import createDB
from app.src.utils.miscFunctions import createKaleidoFolder, whatPlatform, changeTheme
from pathlib import Path
import asyncio

lang = "en"

class Kaleido(App):
    ENABLE_COMMAND_PALETTE = False
    
    BINDINGS = [("q, ctrl+c", "quit", "Close"),
                ("1", "change_theme('minecraft')", "Minecraft Theme"),
                ("2", "change_theme('nether')", "Nether Theme"),
                ("3", "change_theme('end')", "End Theme"),
                ]
    
    TITLE = "Kaleido - Launcher"
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
    
    @work
    async def on_mount(self) -> None:
        self.register_theme(MyThemes.minecraft_theme)
        self.register_theme(MyThemes.nether_theme)
        self.register_theme(MyThemes.end_theme)
        
        platformPath = whatPlatform()
        
        await asyncio.to_thread(createKaleidoFolder, platformPath)
        await asyncio.to_thread(createDB)
        
        themePath = Path(platformPath / ".theme")
        langPath = Path(platformPath / ".lang")
        
        if not themePath.exists():
            with themePath.open("w") as file:
                file.write("end")
        
        with themePath.open("r") as file:
            self.theme = file.read()
            
        if not langPath.exists():
            self.push_screen(SelectLanguage())
            return
        
        global lang
        
        with langPath.open("r") as file:
            if file.read().strip() == "SPA":
                lang = "es"
                            
        self.push_screen(Profiles())
    
    def action_change_theme(self, themeName: str) -> None:
        self.theme = themeName
        changeTheme(themeName)
        
def main():
    app = Kaleido()
    app.run()
    
if __name__ == "__main__":
    main()