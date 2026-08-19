from pydantic import BaseModel


class BlogCreate(BaseModel):
    title : str
    context : str

# Output Schema

class BlogResponse(BaseModel):
    id : int
    title : str
    context : str

class Config:
    from_attribute = True

