from sqlalchemy import Column, Integer, String
from db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    salary = Column(Integer)

    def __repr__(self):
        return '<user %r>' % (self.id)
