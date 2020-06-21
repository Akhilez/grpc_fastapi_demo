from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class BasicModel(Base):
    __tablename__ = "basic"

    id = Column(Integer, primary_key=True)
    column_1 = Column(String)
    column_2 = Column(String)
    column_3 = Column(Integer)

    def __repr__(self):
        return f"BasicModel({self.id}, {self.column_1}, {self.column_2}, {self.column_3})"