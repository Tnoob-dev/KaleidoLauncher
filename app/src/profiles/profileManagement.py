import json
from ..utils.typo import Profile
from ..utils.miscFunctions import whatPlatform
from typing import Dict
from pathlib import Path

def checkProfileFileExistence(profilesPath: Path) -> bool:
    
    if not profilesPath.exists():
        return False

    return True

def createProfileFile(profilesPath: Path) -> bool:
    
    with profilesPath.open(mode="w") as file:
        file.write("")
        
    return True

def addNewProfile(profile: Profile) -> bool:
    
    platform = whatPlatform()
    profilesPath = Path(platform) / "kaleidoProfiles.json"
    
    dataSchema = {
        "username": profile.username,
        "version": profile.version,
        "api": profile.api,
        "minecraftPath": profile.minecraftPath
    }
    
    if not checkProfileFileExistence(profilesPath):
        createProfileFile(profilesPath)
    
    with profilesPath.open("a+") as file:
        json.dump(dataSchema, file, indent=4)
        
def readProfiles(profilesPath: Path) -> Profile:
    
    with profilesPath.open("r") as file:
        
        data = json.load(file)
        
    return Profile(
        username=data["username"],
        version=data["version"],
        api=data["api"],
        minecraftPath=data["minecraftPath"]
    )