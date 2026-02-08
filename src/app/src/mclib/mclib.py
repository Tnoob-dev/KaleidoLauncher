from minecraft_launcher_lib.utils import get_available_versions
from minecraft_launcher_lib.install import install_minecraft_version
from minecraft_launcher_lib.command import get_minecraft_command
from pathlib import Path
from typing import Dict
from ..utils.miscFunctions import createMinecraftFolder
import subprocess


def get_mc_versions(mcPath: Path):
    return [
        ver["id"]
        for ver in get_available_versions(mcPath)
        if ver["type"] == "release"
    ][:40]
    
def install_mc(version: str, mcPath: Path, callback: Dict = None):
    createMinecraftFolder(mcPath)
    
    install_minecraft_version(version, Path(mcPath / ".minecraft"), callback)
    
def execute_mc(username: str, mcVersion: str, mcPath: Path, player_uuid: str):
    
    options = {
        "username": username,
        "uuid": player_uuid,
        "token": ""
    }
    commands = get_minecraft_command(
        version=mcVersion,
        minecraft_directory=Path(Path(mcPath) / ".minecraft"),
        options=options
    )
    
    subprocess.run(commands)