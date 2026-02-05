from sqlmodel import SQLModel, Field, create_engine
from ..utils.miscFunctions import whatPlatform
from pathlib import Path
from typing import Optional

class ProfileTable(SQLModel, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(default=None)
    version: str = Field(default=None)
    api: str = Field(default=None)
    minecraftPath: str = Field(default=whatPlatform())
    uuid: str = Field(default=None, unique=True)
    
DB_PATH = Path(whatPlatform() / "profiles.db")

engine = create_engine(f"sqlite:///{DB_PATH}")

def createDB():
    if not DB_PATH.exists():
        SQLModel.metadata.create_all(engine)