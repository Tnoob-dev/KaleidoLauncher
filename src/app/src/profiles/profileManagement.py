from ..db.dbCreation import ProfileTable, engine
from pathlib import Path
from sqlmodel import Session, select
from typing import List, Optional

def addNewProfile(profile: ProfileTable):
    with Session(engine) as session:
        try:
            session.add(profile)
            session.commit()
        except Exception as e:
            session.rollback()
            raise BaseException(e)

def readProfiles() -> List[ProfileTable]:
    with Session(engine) as session:
        statement = select(ProfileTable)
        result = session.exec(statement).all()

        return [res for res in result]

def getProfileByUsername(username: str) -> Optional[ProfileTable]:
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
            raise BaseException(e)

def updateVersion(username: str, version: str):
    with Session(engine) as session: 
        try:
            statement = select(ProfileTable).where(ProfileTable.username == username)
            user = session.exec(statement).first()
            
            user.version = version
            session.add(user)
            
            session.commit()
            session.refresh(user)
        except Exception as e:
            session.rollback()
            raise BaseException(e)        