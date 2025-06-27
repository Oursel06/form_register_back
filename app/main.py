from fastapi import FastAPI
from app.routes import users
from app.database import get_db
from app.models import User
import bcrypt
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Pour permettre les requêtes CORS depuis localhost et prod
origins = [
    "http://localhost:3000",
    "https://oursel06.github.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "FastAPI Ok"}


@app.on_event("startup")
def create_admin():
    db = next(get_db())
    email = os.getenv("ADMIN_EMAIL")
    password = os.getenv("ADMIN_PASSWORD")
    existing = db.query(User).filter_by(email=email).first()
    if not existing:
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        admin_user = User(
            email=email,
            password=hashed_pw,
            firstname="Admin",
            lastname="User",
            is_admin=True
        )
        db.add(admin_user)
        db.commit()