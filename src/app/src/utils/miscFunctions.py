from pathlib import Path
from typing import Optional
from minecraft_launcher_lib.mod_loader import list_mod_loader
import os
import platform
import uuid

def whatPlatform() -> Path:
    match platform.system().lower():
        case "linux" | "darwin":
            return Path.home() / "Kaleido"
        case "windows":
            return Path(os.getenv("APPDATA")) / "Kaleido"

def createKaleidoFolder(path: Path) -> bool:
    if path.exists():
        return False

    path.mkdir()
    return True

def createMinecraftFolder(mcPath: Optional[Path] = None) -> bool:

    if not mcPath:
        pathToFolder = Path(whatPlatform()) / ".minecraft"

    pathToFolder = Path(mcPath) / ".minecraft"

    if pathToFolder.exists():
        return False

    pathToFolder.mkdir()
    return True

def createUUID(username: str):
    return str(uuid.uuid3(uuid.NAMESPACE_DNS, username))

def changeTheme(newTheme: str):

    kaleidoPath = Path(whatPlatform()) / ".theme"

    with kaleidoPath.open("w") as file:
        file.write(newTheme)

def createLangFile(spanish = False, english = False):

    kaleidoPath = Path(whatPlatform()) / ".lang"

    with kaleidoPath.open("w") as file:
        if spanish and not english:
            file.write("SPA")
        elif english and not spanish:
            file.write("ENG")

def displayModLoaders():
    return list_mod_loader()

def getMinecraftVersion(path: Path) -> str:
    
    versionPath = Path(path) / Path(".minecraft") / Path("versions")
    
    versions = versionPath.iterdir()
    
    
    keywords = ["forge", "neoforge", "fabric", "quilt"]
    
    modLoader = []
    
    for ver in versions:
        modLoader.append(str(ver).split("/")[-1])
    
    if len(modLoader) >= 2:
        modLoader.pop(0)
        
    for key in keywords:
        return modLoader[0] if key in modLoader[0] else "vanilla"