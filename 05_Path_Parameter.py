from fastapi import FastAPI, Query, Path
from typing import Annotated

app = FastAPI()

#If the parameters are not defined in the function
@app.get("/")
async def get_root():
    return {"Hello": "World"}

#declare metadata, use title
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

#Number validation
# ge, le: greater(less) than or equal to
# gt, lt: We can replace ge with gt, lt
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(ge=1)], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

#float also work
@app.get("/items2/{item_id}")
async def read_items(
    item_id: Annotated[float, Path(gt=1)], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

