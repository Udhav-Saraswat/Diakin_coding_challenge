from fastapi import FastAPI, Request, Body
import uvicorn
from fastapi.encoders import jsonable_encoder
from pydantic import BaseConfig

from src.dto.Building import Building
from src.dto.Room import Room, Status
from src.service.BuildingService import BuildingService, build_in_memory_data
from typing import Any

fastapi = FastAPI()
BaseConfig.arbitrary_types_allowed = True


def run_server():
    build_in_memory_data()
    uvicorn.run(fastapi, host="127.0.0.1", port=8080)


@fastapi.get("/getBuildingDetails")
async def get_buildings() -> Any:
    return BuildingService.get_buildings()


@fastapi.post("/addRooms", status_code=201)
async def add_rooms(payload: Any = Body(None)) -> Any:
    res = BuildingService.add_rooms(payload)
    return jsonable_encoder(res)
