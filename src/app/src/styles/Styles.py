class Styles:
    profileScreen: str = """
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

    dashboardScreen = """

.hidden {
    display: none;
}

#dashboard {
    height: 100%;
    margin: 4 8;
    background: $panel;
    color: $text;
    border: tall $background;
    padding: 1 2;
    layout: vertical;
}

Button {
    width: 1fr;
}

.info_static {
    text-style: bold;
    height: auto;
    content-align: center middle;
    margin-bottom: 2;
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