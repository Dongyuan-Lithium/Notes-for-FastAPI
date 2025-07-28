from fastapi import FastAPI, Query
from typing import Annotated
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
    return {"Hello": "World"}

#Annotated does not effect anything in python 
#but it helps Fastapi to get extra limitation on the vars (aka validation)
@app.get("/items/{item}")
async def get_item(item : Annotated[int | None, Query(max_length=50)]):
    return {"item": item}

#Old version
@app.get("/items2/{item}")
async def get_items(item : int | None = Query(default=None, max_length=50))
    return {"item": item}

#regex can be used
@app.get("/items3/{item}")
async def get_item(item : Annotated[int | None, Query(pattern="*/")] = None):
    return {"item": item}

#same for query parameters (None also acceptable)
@app.get("/items4/{q}")
async def get_item(q : Annotated[int | None, Query(pattern="*/")]):
    return {"q": q}

#list of queries/ Used because query is defaulted to be string
    #Has type
@app.get("/items5/{q}")
async def get_item(q : Annotated[list[int] | None, Query(pattern="*/")]):
    return {"q": q}

    #No type
@app.get("/items5/{q}")
async def get_item(q : Annotated[list | None, Query(pattern="*/")]):
    return {"q": q}

#if var is not accepted in python naming policy
@app.get("/items5/{q}")
async def get_item(q : Annotated[list[int] | None, Query(alias="tis-not-allowed")]):
    return {"q": q}

#if a parameter is no longer needed, use deprecated
@app.get("/items5/{q}")
async def get_item(q : Annotated[list[int] | None, Query(deprecated=True)]):
    return {"q": q}