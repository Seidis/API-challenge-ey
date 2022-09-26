from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base as Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = 'users'
    id = Column('user_id',Integer, primary_key=True)
    name = Column(String)
    tax_id = Column(String)
    telephone = Column(String)
    birth_date = Column(DateTime)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    role = Column(String)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
