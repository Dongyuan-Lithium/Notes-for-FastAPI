from fastapi import FastAPI, Body
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

# To generate clear and beautiful Swagger UI or docs page, we add example metadata,
# use model_config + json_schema_extra + examples
# - it contains a list of dicts
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float 
    tax: float | None = None

    model_config = {
        "json_schema_extra":{
            "examples" : [
                {
                    "name" : "Foo",
                    "description" : "bar",
                    "price" : 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }

# To generate example for one var, use Field
class Item2(BaseModel):
    name : str = Field(examples=["Foo Bar"])

@app.put("/items/")
async def update_items(item_id: int, item: Item | None = None):
    return {"item_id": item_id, "item" : item}

# Want example in body parameters
@app.put("/item2/")
async def update_items(item_id: int, item: Annotated[
    Item,
    Body(
        examples=[
                {
                    "name" : "Foo",
                    "description" : "bar",
                    "price" : 35.4,
                    "tax": 3.2,
                }
        ]
    )
]):
    return {"item_id": item_id, "item": item}