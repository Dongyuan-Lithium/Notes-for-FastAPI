from typing import Annotated
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field

app = FastAPI()

'''
Python knowledge
def func(*, a, b, c):
    print(a, b, c)

func(1, 2, 3)  # ❌ Error (positional not allowed)
func(a=1, b=2, c=3)  # ✔️ Allowed (keyword only)
'''

# An HTTP request has:
# - Start line
#   - method, path, proctocal version
# - Header
# - Body

# Query and Path parameters are in the URL in the start line
# Body parameters are in the JSON body
# - usually more complex with pydantic model



# If single value in body, use Body

@app.put("/items1/")
async def update_item(importance: Annotated[int, Body()]):
    if importance:
        return {"importance": importance}
    


# If JSON type data in body, use pydantic

'''
e.g. in the HTTP body,
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
'''
class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None

@app.put("/items2/")
async def update_item(item: Item | None = None):
    if item:
        return {"item": item}



# If multiple JSON body parameter
'''
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
'''
class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None

class User(BaseModel):
    username: str
    full_name: str

@app.put("/items3/")
async def update_item(item: Item | None = None, user: User | None = None):
    result = {}
    if item:
        result.update({"item", item})
    if user:
        result.update({"user", user})
    return result

