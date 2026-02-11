from textual import work
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Label, Button, Input, Select, RadioSet, RadioButton, Header, Footer
from textual.containers import Horizontal, Vertical
from pathlib import Path
from ..mclib.mclib import get_mc_versions
from ..db.dbCreation import ProfileTable
from ..styles.Styles import Styles
from ..utils.miscFunctions import whatPlatform, createUUID, displayModLoaders
from ..profiles.profileManagement import addNewProfile, readProfiles, getProfileByUsername
from ..langs.Languages import Langs
import asyncio

class ProfileCreation(Screen):
    
    CSS = Styles.profileCreationStyles
    
    def __init__(self, name = None, id = None, classes = None):
        self.platform = whatPlatform()
        super().__init__(name, id, classes)

    def compose(self) -> ComposeResult:
        from app.cli import lang
        
        yield Header()
        yield Footer()
        
        yield Vertical(
            Horizontal(
                Label(Langs.langsDict["profileUsernameLabel"][lang], id="name_label"),
                Input(placeholder="Steve", id="name_input").focus(),
                classes="form-row"
            ),
            Horizontal(
                Label(Langs.langsDict["pathLabel"][lang], id="ubi_label"),
                Input(str(Path(self.platform)), id="ubi_input"),
                classes="form-row"
            ),
            
            Horizontal(
                Label(Langs.langsDict["versionLabel"][lang], id="version_label"),
                Vertical(
                    Select([], prompt="", id="version_select"),
                    Label("", id="error_label", classes="hidden"),
                    Button(Langs.langsDict["retryButton"][lang], id="retry_connection_btn", classes="hidden"),
                ),
                classes="form-row"
            ),
            RadioSet(
                    RadioButton("Vanilla", value=True),
                    # display every mod loader
                    *[
                        RadioButton(label=label.capitalize())
                        for label in displayModLoaders()
                    ],
                    id="radio_set_apis"
                ),
            Vertical(
                Button(Langs.langsDict["createButton"][lang], id="create_btn", disabled=True, classes="submit-btn"),
            ),
            id="form-container"
        )

    @work   
    async def on_mount(self) -> None:
        
        selectVersionWidget = self.query_one("#version_select", Select)
        
        
        tempPath = Path(self.platform)
        
        releases = await asyncio.to_thread(get_mc_versions, tempPath)
        
        if len(releases) > 0 :
            selectVersionWidget.set_options([(release, release) for release in releases])
        else:
            await self.load_versions()
    
    @work
    async def load_versions(self) -> None:
        from app.cli import lang
        try:
            
            tempPath = Path(self.platform)
            
            releases = await asyncio.to_thread(get_mc_versions, tempPath)
            if releases:
                self.query_one("#version_select", Select).set_options([(release, index) for index, release in enumerate(releases)])
                self.update_ui_state("success")
            else:
                self.update_ui_state("error", Langs.langsDict["connectionError"][lang])
        except (Exception, ConnectionError) as e:
            self.update_ui_state("error", Langs.langsDict["connectionErrorSeveral"][lang].format(error=str(e)))

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
        ubiInput = self.query_one("#ubi_input", Input)
        createButton = self.query_one("#create_btn", Button)
        selectVersionWidget = self.query_one("#version_select", Select)
        
        
        fullPath = Path(ubiInput.value)
        
        match event.button.id:
            case "retry_connection_btn":
                
                releases = await asyncio.to_thread(get_mc_versions , fullPath)
                
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
                username = nameInput.value
                
                profile = ProfileTable(
                    username=username,
                    version=selectVersionWidget.value,
                    api=self.get_selected_api(),
                    # verification for funny users lol
                    minecraftPath=str(fullPath) if str(fullPath) != "." else str(Path(whatPlatform())),
                    uuid=createUUID(username),
                    preferredTheme="end"
                )
                addNewProfile(profile)
                
                self.app.push_screen(Profiles())


##########################################################

class Profiles(Screen):
    
    CSS = Styles.profileScreen
    
    def compose(self) -> ComposeResult:
        from app.cli import lang
        
        profiles = readProfiles()
        
        yield Header()
        yield Footer()

        if len(profiles) <= 0:
            yield Button(Langs.langsDict["createButton"][lang], id="create_profile_btn")
            return
        
        for i in range(len(profiles)):
            yield Button(
                label=profiles[i].username,
                id=f"enter_profile_btn{i}",
                classes="profile_boxes"
            )
        
        if len(profiles) < 9:
            yield Button(Langs.langsDict["createButton"][lang], id="create_profile_btn")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "create_profile_btn":
            self.app.push_screen(ProfileCreation())
        elif event.button.id.startswith("enter_profile_btn"):
            username = str(event.button.label)
            
            self.profile = getProfileByUsername(username)
            
            from .DashboardScreen import Dashboard
            self.app.push_screen(Dashboard(self.profile))