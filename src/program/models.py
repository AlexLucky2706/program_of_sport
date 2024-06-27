from sqlalchemy import Column, String, Integer, ForeignKey
from database import Base

class Exercise(Base):
    __tablename__ = 'exercise'

    id = Column(Integer, primary_key=True)
    part_of_body = Column(String)
    exercise1 = Column(String)
    exercise2 = Column(String)
    exercise3 = Column(String)

class Program(Base):

    __tablename__ = 'program'

    id = Column(Integer, primary_key=True)
    complect1 = Column(Integer, ForeignKey("exercise.id"))
    complect2 = Column(Integer, ForeignKey("exercise.id"))
    complect3 = Column(Integer, ForeignKey("exercise.id"))
    day1 = Column(String)
    day2 = Column(String)
    day3 = Column(String)
