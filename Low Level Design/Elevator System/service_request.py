from request import Request
from enums import ElevatorType, RequestOrigin

class ServiceRequest(Request):
    def __init__(self, origin: RequestOrigin, current_floor: int=None, destination_floor: int=None):
        if current_floor is not None and destination_floor is not None:
            super().__init__(origin, current_floor, destination_floor)
        else:
            super().__init__(origin, destination_floor)

        self.__elevator_type = ElevatorType.SERVICE

    def get_elevator_type(self):
        return self.__elevator_type