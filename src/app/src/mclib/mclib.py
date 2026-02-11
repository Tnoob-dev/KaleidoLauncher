from minecraft_launcher_lib.utils import get_available_versions
from minecraft_launcher_lib.install import install_minecraft_version
from minecraft_launcher_lib.mod_loader import get_mod_loader
from minecraft_launcher_lib.command import get_minecraft_command
from minecraft_launcher_lib.types import CallbackDict, MinecraftOptions
from pathlib import Path
from typing import List
from ..utils.miscFunctions import createMinecraftFolder
import subprocess

def get_mc_versions(mcPath: Path) -> List[str]:
    return [
        ver["id"]
        for ver in get_available_versions(mcPath)
        if ver["type"] == "release"
    ][:40]

_MOD_LOADER_FUNCTS = {
    "vanilla": lambda version, mcPath, callback: install_minecraft_version(version, Path(mcPath) / ".minecraft", callback),
    "forge": lambda version, mcPath, callback: get_mod_loader("forge").install(version, Path(mcPath) / ".minecraft", callback=callback),
    "neoforge": lambda version, mcPath, callback: get_mod_loader("neoforge").install(version, Path(mcPath) / ".minecraft", callback=callback),
    "fabric": lambda version, mcPath, callback: get_mod_loader("fabric").install(version, Path(mcPath) / ".minecraft", callback=callback),
    "quilt": lambda version, mcPath, callback: get_mod_loader("quilt").install(version, Path(mcPath) / ".minecraft", callback=callback),
}

def minecraftInstall(api: str, version: str, mcPath: Path, callback: CallbackDict) -> None:
    modLoader = api.lower()
    createMinecraftFolder(mcPath)
    
    _MOD_LOADER_FUNCTS[modLoader](version, mcPath, callback)

    # install_minecraft_version(version, Path(mcPath / ".minecraft"), callback)

    
def execute_mc(username: str, mcVersion: str, mcPath: Path, player_uuid: str) -> None:

    options: MinecraftOptions = {
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