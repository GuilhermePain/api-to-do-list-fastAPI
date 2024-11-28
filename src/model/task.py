from pydantic import BaseModel

class CreateTask(BaseModel):
    name: str
    user_id: int
    status: str