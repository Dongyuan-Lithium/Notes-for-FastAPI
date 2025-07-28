from fastapi import FastAPI

app = FastAPI()

#If the parameters are not defined in the function
@app.get("/")
async def get_root():
    return {"message": "default"}

@app.get("/items1")
async def get_item(foo: int = 0, q: str | None = None):
    output = {"foo": foo}
    if q:
        output['q'] = q
        return output
    return output

#Type Bool: "/bar=True" or "/bar=true" or "/bar=on" or "/bar=yes" can all work
@app.get("/items2")
async def get_item(bar : bool = True):
    return {"bar": bar}

#If no default, then required
@app.get("/items3")
async def get_item(bar : bool):
    return {"bar": bar}