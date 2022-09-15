from typing import Optional
from pydantic import BaseModel

class ProductsSchema(BaseModel):
    title: str
    image: str
    likes : list = []