from pydantic import BaseModel
from pathlib import Path

class Releases(BaseModel):
    id: str
    type: str
    url: str
    yearReleased: int
    
class Profile(BaseModel):
    username: str
    version: str
    api: str
    minecraftPath: str