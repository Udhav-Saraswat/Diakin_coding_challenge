from pydantic import BaseModel
from typing import Union, Optional
import random
from enum import Enum
from src.dto.Room import Room


class Building(object):
    room: []
    requestedTemp = 20

    def __init__(self, room):
        self.room = room

    def change_temp(self, changed_temp):
        self.requestedTemp = changed_temp
        for r in self.room:
            Room.update_status(r, changed_temp)

    def add_rooms(self, room):
        self.room.append(room)

    def remove_rooms(self, room):
        self.room.remove(room)

    # def __repr__(self):
    #     return "Test a:% s b:% s" % (self.a, self.b)
    #
    # def __str__(self):
    #     return "From str method of Test: a is % s, " \
    #            "b is % s" % (self.a, self.b)
