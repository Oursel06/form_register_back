from sqlalchemy import Column, Integer, String, Date, Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    firstname = Column(String(255))
    lastname = Column(String(255))
    birthdate = Column(String(255))
    city = Column(String(255))
    postal_code = Column(String(255))
    is_admin = Column(Boolean, default=False)