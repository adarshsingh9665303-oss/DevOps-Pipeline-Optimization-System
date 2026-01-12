from pydantic import BaseModel

class Pipeline(BaseModel):
    id: int
    name: str
    stage: str
    status: str
