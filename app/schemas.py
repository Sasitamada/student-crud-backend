from pydantic import BaseModel


class StudentCreate(BaseModel):
    name: str
    course: str


class StudentUpdate(BaseModel):
    name: str
    course: str


class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True
