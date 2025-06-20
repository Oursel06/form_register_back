from fastapi import APIRouter, HTTPException, Depends
from app.auth import admin_required
from sqlalchemy.orm import Session
from app import database, models, schemas
import jwt
import bcrypt
from datetime import datetime, timedelta
import os

router = APIRouter()

SECRET_KEY = os.getenv("SECRET_KEY", "lid5s6x64k6545f4dx4u96k5621s1c51c54d5g4h54h5jyjtrscdvdgr654b15f5h4t")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        birthdate=user.birthdate,
        city=user.city,
        postal_code=user.postal_code,
        password=user.password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):
    user = db.query(models.User).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")
    
    db.delete(user)
    db.commit()
    return {"message": "Utilisateur supprimé"}

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter_by(email=email).first()
    if not user or not bcrypt.checkpw(password.encode(), user.password.encode()):
        raise HTTPException(status_code=401, detail="Identifiants invalides")
    
    token_data = {
        "email": user.email,
        "is_admin": user.is_admin,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }
    token = jwt.encode(token_data, SECRET_KEY, algorithm="HS256")
    return {"access_token": token}
