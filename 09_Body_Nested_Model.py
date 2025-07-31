from fastapi import FastAPI, Body
from pydantic import BaseModel, HttpUrl
from typing import Annotated

app = FastAPI()

#list
class Item(BaseModel):
    name: str | None = None
    tags : list = []
    tags2 : list[str] = []

#set
class Item1(BaseModel):
    name: str | None = None
    tags : set = set()
    tags2 : set[str] = str()

#submodel and special types
class Item2(BaseModel):
    submodel: Item1 | None = None
    url : HttpUrl
    dictionaries: dict[int, float]
    # JSON only supports string as keys, but pydantic is useful here

@app.put("/items/")
async def update_item(item_id: int, item: Item, item1: Item1, item2: Item2):
    return {"item_id" : item_id, "item" : item}