from pydantic import BaseModel, HttpUrl

from typing import Sequence

class App_Schema(BaseModel):
    #task_id:int
    task: str
    priority: int