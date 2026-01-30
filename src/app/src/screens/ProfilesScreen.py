from textual import work
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Label, Button, Input, Select, RadioSet, RadioButton
from textual.containers import Horizontal, Vertical
from pathlib import Path
from ..mclib.mclib import get_mc_versions
from ..utils.fileHandling import checkPathExists
from ..utils.typo import Profile
from ..utils.miscFunctions import whatPlatform
from ..profiles.profileManagement import addNewProfile, readProfiles
from .DashboardScreen import Dashboard
import asyncio

class ProfileCreation(Screen):

    def compose(self) -> ComposeResult:
        yield Vertical(
        Horizontal(
            Label("Nombre del perfil:", id="name_label"),
            Input(placeholder="Steve", id="name_input").focus(),
            Label("Versión:", id="version_label"),
            Vertical(
                Select([], prompt="", id="version_select"),
                Label("", id="error_label", classes="hidden"),
                
                RadioSet(
                    RadioButton("Vanilla", value=True),
                    RadioButton("Fabric"),
                    RadioButton("Forge"),
                    id="radio_set_apis"
                    ),
                
                Button("Reintentar", id="retry_connection_btn", classes="hidden"),
            ),
            classes="form-row"
        ),
        # Create Button
        Button("Crear", id="create_btn", disabled=True, classes="submit-btn"),
        id="form-container"
    )

    @work   
    async def on_mount(self) -> None:
        
        selectVersionWidget = self.query_one("#version_select", Select)
        
        platform = whatPlatform()
        fullPath = Path(platform / ".minecraft")
        
        releases = await asyncio.to_thread(get_mc_versions, fullPath)
        
        if len(releases) > 0 :
            selectVersionWidget.set_options([(release, release) for release in releases])
        else:
            await self.load_versions()
    
    @work
    async def load_versions(self) -> None:
        
        try:
            platform = whatPlatform()
            fullPath = Path(platform / ".minecraft")
            
            releases = await asyncio.to_thread(get_mc_versions, fullPath)
            if releases:
                self.query_one("#version_select", Select).set_options([(release, index) for index, release in enumerate(releases)])
                self.update_ui_state("success")
            else:
                self.update_ui_state("error", "No se pudo establecer conexion. Revise su conexion a internet")
        except (Exception, ConnectionError) as e:
            self.update_ui_state("error", f"No se pudo establecer conexión: {str(e)}")

    def update_ui_state(self, state: str, error_message: str = "") -> None:
        
        widgets = {
            "name_label": self.query_one("#name_label", Label),
            "version_label": self.query_one("#version_label", Label),
            "name_input": self.query_one("#name_input", Input),
            "create_btn": self.query_one("#create_btn", Button),
            "select": self.query_one("#version_select", Select),
            "error_label": self.query_one("#error_label", Label),
            "retry_btn": self.query_one("#retry_connection_btn", Button),
        }

        if state == "success":
            
            for widget in ["name_label", "version_label", "name_input", "create_btn"]:
                widgets[widget].remove_class("hidden")
                
            widgets["select"].display = True
            widgets["error_label"].add_class("hidden")
            widgets["retry_btn"].add_class("hidden")
            
        elif state == "error":
            
            for widget in ["name_label", "version_label", "name_input", "create_btn"]:
                widgets[widget].add_class("hidden")
            widgets["select"].display = False
            widgets["error_label"].update(error_message)
            widgets["error_label"].remove_class("hidden")
            widgets["retry_btn"].remove_class("hidden")
    
    def on_select_changed(self, event: Select.Changed) -> None:
        self._disableButtonHelper()
    
    def on_input_changed(self, event: Input.Changed) -> None:
        self._disableButtonHelper()
        
    def get_selected_api(self) -> str:
        radioSetWidget = self.query_one("#radio_set_apis", RadioSet)
        
        return str(radioSetWidget.pressed_button.label)
        
    def _disableButtonHelper(self) -> None:
        inputWidget = self.query_one("#name_input", Input)
        selectVersionWidget = self.query_one("#version_select", Select)
        disabledButton = self.query_one("#create_btn", Button)
        
        validName = len(inputWidget.value.strip()) >= 4
        selectedVersion = not selectVersionWidget.is_blank()
        
        disabledButton.disabled = not (validName and selectedVersion)

    @work
    async def on_button_pressed(self, event: Button.Pressed):
        nameLabel = self.query_one("#name_label", Label)
        versionLabel = self.query_one("#version_label", Label)
        errorLabel = self.query_one("#error_label", Label)
        retryButton = self.query_one("#retry_connection_btn", Button)
        nameInput = self.query_one("#name_input", Input)
        createButton = self.query_one("#create_btn", Button)
        selectVersionWidget = self.query_one("#version_select", Select)
        
        platform = whatPlatform()
        fullPath = Path(platform / ".minecraft")
        
        match event.button.id:
            case "retry_connection_btn":
                
                releases = await asyncio.to_thread(get_mc_versions ,fullPath)
                
                if len(releases) > 0:
                    selectVersionWidget.set_options([(release, index) for index, release in enumerate(releases)])
                    
                    nameLabel.remove_class("hidden")
                    versionLabel.remove_class("hidden")
                    errorLabel.add_class("hidden")
                    retryButton.add_class("hidden")
                    nameInput.remove_class("hidden")
                    createButton.remove_class("hidden")
                    
                    selectVersionWidget.display = True
            case "create_btn":
                profile = Profile(
                    username=nameInput.value,
                    version=selectVersionWidget.value,
                    api=self.get_selected_api(),
                    minecraftPath=str(fullPath)
                )
                addNewProfile(profile)
                
                self.app.push_screen(Profiles())


##########################################################

class Profiles(Screen):
    
    def compose(self) -> ComposeResult:
        platform = whatPlatform()
        fullConfigPath = Path(platform / "kaleidoProfiles.json")
        
        fileExists = checkPathExists(fullConfigPath)
            

        if not fileExists:
            yield Label("No existe archivo de configuracion", id="no_config_label")
            yield Button("Crear Nuevo Perfil", id="create_profile_btn")
            return

        self.profile = readProfiles(fullConfigPath)
        
        yield Label("Selecciona un perfil")
        yield Button(
            label=self.profile.username,
            id="enter_profile_btn"
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "create_profile_btn":
            self.app.push_screen(ProfileCreation())
        elif event.button.id == "enter_profile_btn":
            self.app.push_screen(Dashboard(self.profile))
        