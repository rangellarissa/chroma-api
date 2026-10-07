from pydantic import BaseModel

class Color(BaseModel):
    id: int
    name: str
    code: str
    user_id: int

class ColorCreate(BaseModel):
    name: str
    code: str
    user_id: int

class ColorChange(BaseModel):
    name: str | None = None
    code: str | None = None

class ColorWheel(BaseModel):
    id: int
    name: str
    colors: list[Color]
    user_id: int

class ColorWheelCreate(BaseModel):
    name: str
    user_id: int
    color_ids: list[int]