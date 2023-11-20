from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/") # / yol belgisi
async def read_root():
    return{"Hello": "World"}


@app.get("/yol/{bu_yol_parametri}")
async def read_yol(bu_yol_parametri: int, uzgaruvchi: Union[str, None] = None):
    return {"yol_id": bu_yol_parametri, "uzgaruvchi":uzgaruvchi}