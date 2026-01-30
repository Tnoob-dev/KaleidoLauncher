from pathlib import Path
import shutil

def checkPathExists(path: Path) -> bool:
    if not path.exists():
        return False
    
    return True

def removeDir(path: Path):
    try:
        shutil.rmtree(path, ignore_errors=True)
    except Exception as e:
        raise ValueError(f"La ruta proporcionada no es un directorio: {path}")