from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()


#Recall:
# - Path parameter is
#   - always needed
#   - included in the path
# - Query parameter is
#   - needed when not defaulted
#   - not included in the path


#If the parameters are not defined in the function
@app.get("/")
async def get_root():
    return {"Hello": "World"}

#Annotated does not effect anything in python 
#but it helps Fastapi to get extra limitation on the vars (aka validation)
#if want str to limit length, use max_length
@app.get("/items/")
async def get_item(item : Annotated[str | None, Query(max_length=50)] = None):
    return {"item": item}

#Old version
@app.get("/items2/")
async def get_items(item : str | None = Query(default=None, max_length=50)):
    return {"item": item}

#regex can be used
@app.get("/items3/")
async def get_item(item : Annotated[str | None, Query(pattern="^item_[0-9]+$")] = None):
    return {"item": item}

#same for query parameters (None also acceptable)
@app.get("/items4/")
async def get_item(q : Annotated[str | None, Query(pattern="^item_[0-9]+$")] = None):
    return {"q": q}

#list of queries/ Used because query is defaulted to be string
    #Has type
    #/items5/?q=1&q=2
@app.get("/items5/")
async def get_item(q : Annotated[list[str] | None, Query()] = None):
    return {"q": q}

    #No type
@app.get("/items6/")
async def get_item(q : Annotated[list | None, Query()] = None):
    return {"q": q}

#if var is not accepted in python naming policy
@app.get("/items7/")
async def get_item(q : Annotated[list[int] | None, Query(alias="tis-not-allowed")] = None):
    return {"q": q}

#if a parameter is no longer needed, use deprecated
@app.get("/items8/")
async def get_item(q : Annotated[list[int] | None, Query(deprecated=True)] = None):
    return {"q": q}

#If we want the returned parameter to be hidden, use included_in_schema
#schema means OpenAPI schema
@app.get("/items9/")
async def get_items(
    hidden_q: Annotated[
        str | None,
        Query(
            include_in_schema=False
        ),
    ] = None
):
    if hidden_q:
        return {"hidden_query": hidden_q}
    else:
        return {"hidden_query": "Not Found"}

#Create a self-made validation function, and apply it to Query
#use AfterValidator
from pydantic import AfterValidator
import random

data = {
    "prime1": 2,
    "composite1": 4,
    "prime2": 3,
    "fruit1": "apple",
}

def check_valid_id(id: str):
    if not id.startswith(("prime", "composite")):
        raise ValueError("Must be a prime or composite number")
    return id

@app.get("/items10/")
async def get_items(q: Annotated[str | None, AfterValidator(check_valid_id)] = None):
    if q:
        item = data.get(q)
    else:
        q, item = random.choice(list(data.items()))
    return {"id": q, "item": item}