import platform
from pathlib import Path
import os

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

def createMinecraftFolder() -> bool:
    
    pathToFolder = Path(whatPlatform() / ".minecraft")
    
    if pathToFolder.exists():
        return False
    
    pathToFolder.mkdir()
    return True