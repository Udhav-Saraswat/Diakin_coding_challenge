import json

from src.dto.Building import Building
from src.dto.Room import Room, Status

room = []
building: Building = None


def build_in_memory_data():
    global room
    global building
    room = [Room("Guest-1", 30, Status.DISABLED, Status.DISABLED),
            Room("Guest-2", 10, Status.DISABLED, Status.DISABLED),
            Room("Guest-3", 5, Status.DISABLED, Status.DISABLED),
            Room("Guest-4", 2, Status.DISABLED, Status.DISABLED)]
    building = Building(room)


class BuildingService:

    @classmethod
    def get_buildings(cls):
        from fastapi.encoders import jsonable_encoder
        return jsonable_encoder(building)

    @classmethod
    def add_rooms(cls, json_request):
        try:
            room_add = Room(json_request["occupant_Name"], json_request["current_temp"],json_request["heating_status"], json_request["cooling_status"])
            building.room.append(room_add)
        except:
            raise "Error occurred during json load"
        return room_add


