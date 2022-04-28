
from pydantic import BaseModel

class Story(BaseModel):
    name:str
    description: str
    assignedTo:str
    completed: bool
    date: str

