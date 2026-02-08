class Styles:
    profileScreen = """
Profiles {
    align: center middle;
    color: #ffffff;
    layout: grid;
    grid-size: 3;
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
    height: auto;
    background: transparent;
    color: #EAEFEF;
    text-style: none;
    border: round #EAEFEF;
}
"""

    dashboardScreen = """
.hidden {
    display: none;
}

.dashboard {
    background: $panel;
    color: $text;
}

Button {
    width: 1fr;
    text-style: none;
}

.info_static {
    text-style: bold;
    height: auto;
    content-align: center middle;
}

.buttons {
    width: 100%;
    height: auto;
    dock: bottom;
}

#download_pb {
    height: auto;
    margin: 2 0 0 0;
    color: $accent;
}
"""

    profileCreationStyles = """
ProfileCreation {
    align: center middle;
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
    width: 50%;
}

#version_select {
    width: 50%;
}

#ubi_input {
    width: 50%;
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

#ubi_label {
    margin: 1 0 0 0;
}

#version_label {
    margin: 1 0 0 3;
}

#radio_set_apis {
    margin: 0 0 0 40;
    width: 30%;
}
"""

    language_styles = """
    
/* The same from the docs lol */

#dialog {
    height: 100%;
    margin: 4 8;
    background: $panel;
    color: $text;
    border: tall $background;
    padding: 1 2;
}

Button {
    width: 1fr;
    text-style: none;
}

.question {
    text-style: bold;
    height: 100%;
    content-align: center middle;
}

.buttons {
    width: 100%;
    height: auto;
    dock: bottom;
}
"""