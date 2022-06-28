from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user




####################CD#####################
def get_CD(db: Session, CD_id: int):
    return db.query(models.CD).filter(models.CD.id == CD_id).first()


def get_CD_by_id(db: Session, id: int):
    return db.query(models.CD).filter(models.CD.id == id).first()


def get_CDs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CD).offset(skip).limit(limit).all()


def create_CD(db: Session, CD: schemas.CDCreate):
    db_CD = models.CD(id=CD.id)
    db.add(db_CD)
    db.commit()
    db.refresh(db_CD)
    return db_CD


##############################################################
def get_VINYL(db: Session, VINYL_id: int):
    return db.query(models.VINYL).filter(models.VINYL.id == VINYL_id).first()


def get_VINYL_by_id(db: Session, id: int):
    return db.query(models.VINYL).filter(models.VINYL.id == id).first()


def get_VINYLs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.VINYL).offset(skip).limit(limit).all()


def create_VINYL(db: Session, VINYL: schemas.VINYLCreate):
    db_VINYL = models.VINYL(id=VINYL.id)
    db.add(db_VINYL)
    db.commit()
    db.refresh(db_VINYL)
    return db_VINYL