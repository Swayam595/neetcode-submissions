from collections import deque
import time
from elevator import Elevator
from enums import State
from request import Request

class ServiceElevator(Elevator):
    def __init__(self, current_floor: int, emergency_status: bool):
        super().__init__(current_floor, emergency_status)
        self.__service_queue : deque[Request] = deque()

    def operate(self):
        while self.__service_queue:
            curr_request : Request = self.__service_queue.popleft()

            print()
            print(f"Currently at: {self.get_current_floor()}")

            try:
                time.sleep(1)
                print(curr_request.get_direction(), end = "")
                for _ in range(3):
                    print(". ", end = "", flush = True)
                    time.sleep(0.5)
            except KeyboardInterrupt:
                pass
            except Exception as e:
                print(f"Error: {e}")

            self.set_current_floor(curr_request.get_destination_floor())
            self.set_state(curr_request.get_direction())
            print(f"Arrived at : {self.get_current_floor()}")

            self.open_doors()
            self.wait_for_seconds(3)
            self.close_doors()

        self.set_state(State.IDLE)
        print(f"All requests have been fulfilled, elevator is now {self.get_state()}.")

    def add_request_to_queue(self, request: Request) -> None:
        self.__service_queue.append(request)

    def process_emergency(self):
        self.__service_queue.clear()
        self.set_current_floor(1)
        self.set_state(State.IDLE)
        self.open_doors()
        self.set_emergency_status(True)

        print(f"Queue cleared, current floor is {self.get_current_floor()}. Doors are {self.get_door_state()}")