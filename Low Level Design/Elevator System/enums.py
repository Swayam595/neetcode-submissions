from enum import Enum

class State(Enum):
    IDLE = 1
    UP = 2
    DOWN = 3
    EMERGENCY = 4

class ElevatorType(Enum):
    PASSENGER = 1
    SERVICE = 2

class RequestOrigin(Enum):
    INSIDE = 1
    OUTSIDE = 2

class DoorState(Enum):
    OPEN = 1
    CLOSED = 2 