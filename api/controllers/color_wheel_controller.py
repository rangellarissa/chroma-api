from fastapi import APIRouter, HTTPException, status
from api.schemas import ColorWheel, ColorWheelCreate
from api.services import color_wheel

router = APIRouter(prefix="/wheel")

@router.get("/{wheel_id}", response_model=ColorWheel, status_code=status.HTTP_200_OK)
def get(wheel_id: int):
    result = color_wheel.get(wheel_id)
    if result is None:
        raise HTTPException(404, "color wheel not found")
    return result

@router.get("/user/{user_id}", response_model=list[ColorWheel], status_code=status.HTTP_200_OK)
def get_by_user(user_id: int):
    result = color_wheel.get_by_user(user_id)
    return result

@router.post("", response_model=ColorWheel, status_code=status.HTTP_201_CREATED)
def create(data: ColorWheelCreate):

    result = color_wheel.create(data)
    return result

#@router.patch("/{color_id}", response_model=Color, status_code=status.HTTP_200_OK)
#def change(color_id: int, data: ColorChange):
#    fields = data.model_dump(exclude_unset=True)
#    if not fields:
#        raise HTTPException(400, "nothing to update")

#    result = services.change_color(color_id, fields)

#    if result is None:
#        raise HTTPException(404, "color not found")
    
#    return result

#@router.delete("/{wheel_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
#def delete(wheel_id: int):
#    result = services.delete_color_wheel(wheel_id)

#    if result is None:
#        raise HTTPException(404, "color not found")
