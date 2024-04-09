from pydantic import BaseModel
from typing import Union, Optional
import random
from enum import Enum
import uuid


class Status(Enum):
    ENABLED = "enabled"
    DISABLED = "disabled"


class Room(object):
    temp = int(random.randrange(10, 40))
    uuid: str
    occupant_Name: str
    current_temp = temp
    heating_status: Status.DISABLED
    cooling_status: Status.DISABLED

    def __init__(self, occupant_name, current_temp, heating_status, cooling_status):
        self.uuid = str(uuid.uuid4())
        self.occupant_Name = occupant_name
        self.current_temp = current_temp
        self.heating_status = heating_status
        self.cooling_status = cooling_status

    def update_status(self, request_temp):
        if request_temp <= self.current_temp:
            self.heating_status = Status.DISABLED
            self.cooling_status = Status.ENABLED
        else:
            self.heating_status = Status.ENABLED
            self.cooling_status = Status.DISABLED

    # def __repr__(self):
    #     return "Test a:% s b:% s" % (self.a, self.b)
    #
    # def __str__(self):
    #     return "From str method of Test: a is % s, " \
    #            "b is % s" % (self.a, self.b)
