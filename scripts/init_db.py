# Créer un utilisateur administrateur dans la table users après que la base de données ait été initialisée.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User, Base
from app.database import DB_URL

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def create_admin_user():
    db = SessionLocal()
    try:
        if not db.query(User).filter(User.email == "admin@example.com").first():
            admin = User(
                firstname="Admin",
                lastname="User",
                email="admin@example.com",
                password="hashed_password_here",
                is_admin=True,
            )
            db.add(admin)
            db.commit()
            print("Admin user created!")
        else:
            print("Admin user already exists.")
    finally:
        db.close()

create_admin_user()
