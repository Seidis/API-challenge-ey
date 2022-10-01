from turtle import back
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))
    role = Column(String(20))

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email}, password={self.password}, role={self.role})"


class UserData(Base):
    __tablename__ = "users_data"

    id = Column('id', Integer, primary_key=True, index=True)
    user_id = Column('user_id', Integer, ForeignKey("users.id"), index=True)
    cpf = Column('cpf', String(20), nullable=True)
    telephone = Column('telephone', String(20), nullable=True)
    birth_date = Column('birth_date', Date, nullable=True)

    user = relationship("User", foreign_keys=[
                        user_id], backref=backref("users_data", uselist=False))

    def __repr__(self):
        return f"UserData(id={self.id}, user_id={self.user_id}, cpf={self.cpf}, telephone={self.telephone}, birth_date={self.birth_date})"
