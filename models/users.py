from models import Base

from sqlalchemy import Column, Integer, String, DateTime


class User(Base):
    __tablename__ = 'users'
    id = Column('user_id', Integer, primary_key=True)
    name = Column(String)
    tax_id = Column(String)
    telephone = Column(String)
    birth_date = Column(DateTime)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    role = Column(String)
