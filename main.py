import requests
import uuid
from typing import Annotated
from pydantic import BaseModel, Field, field_validator
from datetime import date, datetime, timedelta
url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v1.json'

response = requests.get(url)
data = response.json()


class Student(BaseModel):
    id: uuid.UUID
    name: str
    date_of_birth: date
    GPA: Annotated[float, Field(ge=0, le=4)]
    course: str | None
    department: str
    fees_paid: bool

    @field_validator('date_of_birth')
    def ensure_16_or_over(cls, value):
        six = datetime.now() - timedelta(days=365*16)
        dix = six.date()
        if value > dix:
            raise ValueError("too young")
        return value

for student in data:
    model = Student(**student)
    print(type(model.model_dump_json()))