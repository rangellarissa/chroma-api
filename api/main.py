from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
print('Hello world')

items: dict[int, dict] = {}

class Chroma(BaseModel):
    code: str
    name: str


@app.post("/chroma-lib", status_code=201)
def create_chroma(chroma: Chroma):
    id = len(items)