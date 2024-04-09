from pprint import pprint
from src.dto.Building import Building
from src.dto.Room import Status, Room
from src.API import BuildingApi
from src.service.SchedulerService import trigger_scheduler

if __name__ == "__main__":

    # adding 4 rooms to the building initially
    room = [Room("Guest-1", 30, Status.DISABLED, Status.DISABLED),
            Room("Guest-2", 10, Status.DISABLED, Status.DISABLED),
            Room("Guest-3", 5, Status.DISABLED, Status.DISABLED),
            Room("Guest-4", 2, Status.DISABLED, Status.DISABLED)]

    building = Building(room)

    building.change_temp(-5)
    """
    changes the cooling/heating status based on change temp 
    """
    for r in building.room:
        pprint(vars(r))

    trigger_scheduler()
    BuildingApi.run_server()
