import json
from pathlib import Path
import typing

def checkConfigExists(path: Path) -> bool:
    if not path.exists():
        return False
    
    return True


