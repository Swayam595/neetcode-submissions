import time
from abc import ABC, abstractmethod
from enums import DoorState, State

class Elevator(ABC):
    def __init__(self, current_floor: int, emergency_status: bool):
        self.current_floor = current_floor
        self.emergency_status = emergency_status
        self.state = State.IDLE
        self.door_state = DoorState.CLOSED

    def open_doors(self) -> None:
        self.door_state = DoorState.OPEN
        print(f"Doors are OPEN on floor: {self.current_floor}.")

    def close_doors(self) -> None:
        self.door_state = DoorState.CLOSED
        print("Doors are CLOSED.")

    def wait_for_seconds(self, seconds: int) -> None:
        time.sleep(seconds)

    def get_current_floor(self) -> int:
        return self.current_floor

    def get_state(self) -> State:
        return self.state

    def set_state(self, state: State) -> None:
        self.state = state

    def set_current_floor(self, floor: int) -> None:
        self.current_floor = floor

    def get_door_state(self) -> DoorState:
        return self.door_state

    def set_emergency_status(self, emergency_status: bool) -> None:
        self.emergency_status = emergency_status

    @abstractmethod
    def operate(self):
        pass

    @abstractmethod
    def process_emergency(self):
        pass