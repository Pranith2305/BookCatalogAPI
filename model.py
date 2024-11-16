from pydantic import BaseModel

class Book(BaseModel):
    id : int
    book_name : str
    author : str
    genre : str
    publish_time : int
    