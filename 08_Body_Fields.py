from fastapi import FastAPI, Body
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

# Similar to Query_Fields
# To make the body must contain the "item", use embed=True
class Item(BaseModel):
    name : str
    description : str = Field(default=None, title="description of the item", max_length=300)
    price : float = Field(gt=0, description="price must be positive")
    tax : float | None = None

@app.put("/items/")
async def update_item(item: Annotated[Item, Body(embed=True)]):
    return {"item": item}


