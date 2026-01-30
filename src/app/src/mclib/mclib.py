from minecraft_launcher_lib.utils import get_available_versions, generate_test_options
from minecraft_launcher_lib.install import install_minecraft_version
from minecraft_launcher_lib.command import get_minecraft_command
from pathlib import Path
from typing import Dict
from textual.widgets import Button
from ..utils.miscFunctions import createMinecraftFolder
import subprocess
import uuid


def get_mc_versions(mcPath: Path):
    return [
        ver["id"]
        for ver in get_available_versions(mcPath)
        if ver["type"] == "release"
    ][:40]
    
def install_mc(version: str, path: Path, callback: Dict = None):
    createMinecraftFolder()
    
    install_minecraft_version(version, path, callback)
    
def execute_mc(username: str, mcVersion: str, mcPath: Path):
    player_uuid = str(uuid.uuid3(uuid.NAMESPACE_DNS, username))
    options = {
        "username": username,
        "uuid": player_uuid,
        "token": ""
    }
    commands = get_minecraft_command(
        version=mcVersion,
        minecraft_directory=mcPath,
        options=options
    )
    
    subprocess.run(commands)