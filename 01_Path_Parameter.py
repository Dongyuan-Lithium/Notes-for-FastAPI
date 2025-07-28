from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"



app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.price, "item_id": item_id}

#Type 1: Enum to limit the type of input
@app.get("/models/{model}")
async def get_model(model : ModelName):
    if model is ModelName.alexnet:
        return{"message": "This model is " + model}
    if model.value == "lenet":
        return{"message": "This model is " + model}

#Type 2: consider paths as an input
@app.get("/paths/{file_path: path}")
async def get_path(file_path: str):
    return {"file_path": file_path}


