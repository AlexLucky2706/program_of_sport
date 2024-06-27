from pydantic import BaseModel

class ProgramCreate(BaseModel):
    complect1: int
    complect2: int
    complect3: int
    day1: str
    day2: str
    day3: str


class ExerciseCreate(BaseModel):
    id: int
    part_of_body: str
    exercise1: str
    exercise2: str
    exercise3: str
