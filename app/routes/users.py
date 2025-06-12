from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import database, models

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users")
def create_user(user: models.User, db: Session = Depends(get_db)):
    db.add(user)
    db.commit()
    return {"message": "Utilisateur enregistré"}

@router.get("/users")
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).filter(models.User.is_admin == False).all()

@router.delete("/users/{user_id}")
def delete_user(user_id: int, email: str, db: Session = Depends(get_db)):
    admin = db.query(models.User).filter_by(email=email, is_admin=True).first()
    if not admin:
        raise HTTPException(status_code=403, detail="Accès refusé")
    
    user = db.query(models.User).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")
    
    db.delete(user)
    db.commit()
    return {"message": "Utilisateur supprimé"}