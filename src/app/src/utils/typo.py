from pydantic import BaseModel
    
class Profile(BaseModel):
    username: str
    version: str
    api: str
    minecraftPath: str
    uuid: str