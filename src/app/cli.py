from textual import work
from textual.app import App, ComposeResult
from textual.widgets import Header
from app.src.screens.ProfilesScreen import Profiles
from app.src.themes.themes import MyThemes
from app.src.utils.miscFunctions import createKaleidoFolder, whatPlatform
import asyncio

class Kaleido(App):
    ENABLE_COMMAND_PALETTE = False
    
    CSS = """
    /* Profile doesnt exists Screen */

Profiles {
    align: center middle;
    color: #ffffff;
    layout: vertical;
    text-style: none;
}

Button {
    text-style: none;
}

Profiles > Label {
    background: #000000;
    align: center middle;
}

#no_config_label {
    content-align-horizontal: center;
    text-style: reverse;
}

#create_profile_btn {
    margin: 2 0 0 6;
    height: auto;
    background: transparent;
    color: #EAEFEF;
    text-style: none;
    border: round #EAEFEF;
}

/* Profile Creation Screen */

ProfileCreation {
    align: center middle;
    padding: 0 -5;
}

#create_btn {
    margin: 0 0 0 50;
    height: auto;
    background: transparent;
    color: #EAEFEF;
    text-style: none;
    border: round #EAEFEF;
}

#name_input {
    width: 30%;
}

#version_select {
    width: auto;
}

.error_label {
    color: #BF616A;
    text-style: bold;
    text-align: center;
    margin: 15 0 0 37;
}

.hidden {
    display: none;
}

#retry_connection_btn {
    margin: 1 0 0 50;
    height: auto;
    background: transparent;
    color: #EAEFEF;
    text-style: none;
    border: round #EAEFEF;
}

.form-row {
    margin: 1 0 0 25;
}

#name_label {
    margin: 1 0 0 0;
}

#version_label {
    margin: 1 0 0 3;
}
    """
    
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