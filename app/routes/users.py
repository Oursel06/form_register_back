from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import database, models, schemas

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # tu peux ici vérifier si email existe déjà etc.
    db_user = models.User(
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        birthdate=user.birthdate,
        city=user.city,
        postal_code=user.postal_code,
        password=user.password,  # idéalement hasher avant de sauvegarder
        is_admin=False
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # récupère les infos générées (ex: id)
    return db_user

@router.get("/users", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    users = db.query(models.User).filter(models.User.is_admin == False).all()
    return users

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
