from fastapi import APIRouter, HTTPException, status
from api.schemas import Color, ColorCreate, ColorChange
from api.services import color

router = APIRouter(prefix="/color")

@router.get("/{color_id}", response_model=Color, status_code=status.HTTP_200_OK)
def get(color_id: int):
    result = color.get(color_id)
    if result is None:
        raise HTTPException(404, "color not found")
    return result

@router.get("/user/{user_id}", response_model=list[Color], status_code=status.HTTP_200_OK)
def get_by_user(user_id: int):
    result = color.get_by_user(user_id)
    return result

@router.post("", response_model=Color, status_code=status.HTTP_201_CREATED)
def create(data: ColorCreate):
    return color.create(data)

@router.patch("/{color_id}", response_model=Color, status_code=status.HTTP_200_OK)
def change(color_id: int, data: ColorChange):
    fields = data.model_dump(exclude_unset=True)
    if not fields:
        raise HTTPException(400, "nothing to update")

    result = color.change(color_id, fields)

    if result is None:
        raise HTTPException(404, "color not found")
    
    return result

@router.delete("/{color_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def delete(color_id: int):
    result = color.delete(color_id)
    if result is None:
        raise HTTPException(404, "color not found")
    return result
