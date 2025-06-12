from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(100), unique=True, index=True)
    birthdate = Column(String(10))
    city = Column(String(50))
    postal_code = Column(String(10))
    password = Column(String(128))
    is_admin = Column(Boolean, default=False)