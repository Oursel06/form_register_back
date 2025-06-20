from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
import jwt
import os

from app import models
from app.database import get_db

security = HTTPBearer()
SECRET_KEY = os.getenv("SECRET_KEY", "default_key")

def admin_required(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    try:
        token = credentials.credentials
        print("Token reçu :", token)
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        print("Payload décodé :", payload)
        email = payload.get("email")

        if not email:
            raise HTTPException(status_code=401, detail="Token invalide (email manquant)")

        user = db.query(models.User).filter(models.User.email == email).first()
        if not user or not user.is_admin:
            raise HTTPException(status_code=403, detail="Accès interdit (admin uniquement)")

        return user

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expiré")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token invalide")
