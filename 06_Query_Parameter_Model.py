from typing import Annotated, Literal
from pydantic import BaseModel, Field
from fastapi import FastAPI, Query

app = FastAPI()

#aggregate parameters and query filters together, two forms
# 1. param: type = default value
# 2. param: type = Field(default value, filter condition) 
#   - Field: includes default value and query filter condition

# After all we write pass FilterParams to Query using Annotated
#   - Annotated[FilterParams, Query()]

class FilterParams(BaseModel):
    limit: int = Field(100, gt = 0, le = 100)
    offset: int = Field(0, ge = 0)
    order_by : Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

@app.get("/")
async def get_root():
    return {"hello": "world"}

@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query

#Forbid unknown parameters
class FilterParams(BaseModel):
    model_config = {"extra" : "forbid"}

    limit: int = Field(100, gt = 0, le = 100)
    offset: int = Field(0, ge = 0)
    order_by : Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

@app.get("/items2/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query