from app import models, database
import os

def init_db():
    models.Base.metadata.create_all(bind=database.engine)

def create_admin():
    db = database.SessionLocal()
    from app.models import User
    admin = db.query(User).filter_by(email=os.getenv("ADMIN_EMAIL")).first()
    if not admin:
        new_admin = User(
            firstname="Loise",
            lastname="Fenoll",
            email=os.getenv("ADMIN_EMAIL"),
            birthdate="1990-01-01",
            city="Paris",
            postal_code="75000",
            is_admin=True
        )
        db.add(new_admin)
        db.commit()
    db.close()