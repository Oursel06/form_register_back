from sqlalchemy import Column, Integer, String, Date, Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(100))
    lastname = Column(String(100))
    email = Column(String(255), unique=True, index=True)
    birthdate = Column(Date)
    city = Column(String(100))
    postal_code = Column(String(20))
    password = Column(String(255))
