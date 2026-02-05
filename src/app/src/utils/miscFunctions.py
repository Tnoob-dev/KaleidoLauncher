from pathlib import Path
import platform
import os
import uuid

def whatPlatform() -> Path:
    match platform.system().lower():
        case "linux":
            return Path.home() / "Kaleido"
        case "windows":
            return Path(os.getenv("APPDATA")) / "Kaleido"
        case "darwin":
            return Path.home() / "Kaleido"
        case _:
            raise OSError("Plataforma no soportada")
        
def createKaleidoFolder(path: Path) -> bool:
    if path.exists():
        return False
    
    path.mkdir()
    return True

def createMinecraftFolder(mcPath: Path = None) -> bool:
    
    if not mcPath:
        pathToFolder = Path(whatPlatform() / ".minecraft")
    
    pathToFolder = Path(mcPath / ".minecraft")
    
    if pathToFolder.exists():
        return False
    
    pathToFolder.mkdir()
    return True

def createUUID(username: str):
    return str(uuid.uuid3(uuid.NAMESPACE_DNS, username))

def changeTheme(newTheme: str):
    
    kaleidoPath = Path(whatPlatform() / ".theme")
    
    with kaleidoPath.open("w") as file:
        file.write(newTheme)
        
def createLangFile(spanish = False, english = False):
    
    kaleidoPath = Path(whatPlatform() / ".lang")
    
    with kaleidoPath.open("w") as file:
        if spanish and not english:
                file.write("SPA")
        elif english and not spanish:
                file.write("ENG")