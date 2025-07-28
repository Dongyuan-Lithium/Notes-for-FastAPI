from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None
    tax: float | None = None

app = FastAPI()

#If the parameters are not defined in the function
@app.get("/")
async def get_root():
    return {"message": "default"}

#Use post, put, delete, patch to send request
# - Function: Send data from client to server/API
#           - the data will be returned to this object
@app.post("/items/")
async def create_item(item: Item):
    return item

#Retrieve the item and return it
@app.post("/items2/{item_id}")
async def create_item(item_id : int, item: Item):
    return {"item_id": item_id, **item.model_dump()}