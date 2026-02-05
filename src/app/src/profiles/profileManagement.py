from ..db.dbCreation import ProfileTable, engine
from pathlib import Path
from sqlmodel import Session, select
from typing import Generator

def checkProfileFileExistence(profilesPath: Path) -> bool:
    
    if not profilesPath.exists():
        return False

    return True

def createProfileFile(profilesPath: Path) -> bool:
    
    with profilesPath.open(mode="w") as file:
        file.write("")
        
    return True

def addNewProfile(profile: ProfileTable) -> bool:    
    try:
        with Session(engine) as session:
            session.add(profile)
            session.commit()
    except Exception as e:
        session.rollback()
        raise str(e)
            
def readProfiles() -> Generator[ProfileTable]:
    with Session(engine) as session:
        statement = select(ProfileTable)
        result = session.exec(statement).all()
        
        return [res for res in result]

def getProfileByUsername(username: str) -> ProfileTable:
    with Session(engine) as session:
        statement = select(ProfileTable).where(ProfileTable.username == username)
        user = session.exec(statement).first()

        return user

def deleteProfiles(username: str):
    with Session(engine) as session:
        try:
            statement = select(ProfileTable).where(ProfileTable.username == username)

            user = session.exec(statement).first()

            session.delete(user)
            session.commit()
            
        except Exception as e:
            session.rollback()
            raise str(e)