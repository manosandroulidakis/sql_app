from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

server_default = 0

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user





########################CD############################################
@app.post("/CD/", response_model=schemas.CD)
def create_CD(CD: schemas.CDCreate, db: Session = Depends(get_db)):
    db_CD = crud.get_CD_by_id(db, id=CD.id)
    if db_CD:
        raise HTTPException(status_code=400, detail="CD already registered")
    return crud.create_CD(db=db, CD=CD)


@app.get("/CD/", response_model=list[schemas.CD])
def read_CDs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    CDs = crud.get_CDs(db, skip=skip, limit=limit)
    return CDs


@app.get("/CD/{CD_id}", response_model=schemas.CD)
def read_CD(CD_id: int, db: Session = Depends(get_db)):
    db_CD = crud.get_CD(db, CD_id=CD_id)
    if db_CD is None:
        raise HTTPException(status_code=404, detail="CD not found")
    return db_CD


########################VINYL############################################
@app.post("/VINYL/", response_model=schemas.VINYL)
def create_VINYL(VINYL: schemas.VINYLCreate, db: Session = Depends(get_db)):
    db_VINYL = crud.get_VINYL_by_id(db, id=VINYL.id)
    if db_VINYL:
        raise HTTPException(status_code=400, detail="VINYL already registered")
    return crud.create_VINYL(db=db, VINYL=VINYL)


@app.get("/VINYL/", response_model=list[schemas.VINYL])
def read_VINYLs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    VINYLs = crud.get_VINYLs(db, skip=skip, limit=limit)
    return VINYLs


@app.get("/VINYL/{VINYL_id}", response_model=schemas.VINYL)
def read_VINYL(VINYL_id: int, db: Session = Depends(get_db)):
    db_VINYL = crud.get_VINYL(db, VINYL_id=VINYL_id)
    if db_VINYL is None:
        raise HTTPException(status_code=404, detail="VINYL not found")
    return db_VINYL