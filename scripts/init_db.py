# Créer un utilisateur administrateur dans la table users après que la base de données ait été initialisée.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User, Base
from app.database import DB_URL
import os
from dotenv import load_dotenv
import bcrypt

load_dotenv()

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def create_admin_user():
    db = SessionLocal()
    try:
        email = os.getenv("ADMIN_EMAIL")
        password = os.getenv("ADMIN_PASSWORD")
        if not db.query(User).filter(User.email == email).first():
            hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            admin = User(
                firstname="Loise",
                lastname="Fenoll",
                email=email,
                password=hashed_pw,
                is_admin=True,
                birthdate="1990-01-01",
                city="Antibes",
                postal_code="06400"
            )
            db.add(admin)
            db.commit()
            print("Admin créé !")
        else:
            print("Admin existe déjà.")
    finally:
        db.close()

if __name__ == "__main__":
    create_admin_user()
