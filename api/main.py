from fastapi import FastAPI

from api.controllers.color_controller import router as color_router
from api.controllers.color_wheel_controller import router as color_wheel_router

app = FastAPI()

app.include_router(color_router)
app.include_router(color_wheel_router)
