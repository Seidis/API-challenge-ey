from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class BaseVagas(Base):
    __tablename__ = 'vagas'

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String(300))
    title = Column(String(100))
    short_description = Column(String(200))
    description = Column(String(1000))
    salary = Column(float, nullable=True)
    location = Column(String(20))
    type = Column(String(20))
    level = Column(String(20))
    is_active = Column(bool)

    def __repr__(self):
        return f"Vagas(id={self.id}, image_url={self.image_url}, title={self.title}, short_description={self.short_description}, description={self.description}, salary={self.salary}, location={self.location}, type={self.type}, level={self.level})"
