from enums import ElevatorType, RequestOrigin, State

class Request:
    def __init__(self, origin: RequestOrigin, origin_floor: int, destination_floor: int = None):
        self.__origin = origin
        self.__origin_floor = origin_floor
        self.__destination_floor = destination_floor if destination_floor is not None else origin_floor

        self.__direction = State.IDLE
        self.__elevator_type = ElevatorType.PASSENGER

        if self.__origin_floor is not None and self.__destination_floor is not None:
            if self.__origin_floor > self.__destination_floor:
                self.__direction = State.DOWN
            elif self.__origin_floor < self.__destination_floor:
                self.__direction = State.UP

    def get_origin_floor(self) -> int:
        return self.__origin_floor

    def get_destination_floor(self) -> int:
        return self.__destination_floor

    def get_origin(self) -> RequestOrigin:
        return self.__origin

    def get_direction(self) -> State:
        return self.__direction

    def get_elevator_type(self) -> ElevatorType:
        return self.__elevator_type

    def __lt__(self, other: "Request") -> bool:
        return self.__destination_floor < other.get_destination_floor()
