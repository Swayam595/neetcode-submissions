import heapq
import time
from elevator import Elevator
from enums import RequestOrigin, State
from request import Request

class PassengerElevator(Elevator):
    def __init__(self, current_floor: int, emergency_status: bool):
        super().__init__(current_floor, emergency_status)
        self.__passenger_up_queue : list[Request] = []
        self.__passenger_down_queue : list[tuple[int, Request]] = []

    def operate(self) -> None:
        while self.__passenger_up_queue or self.__passenger_down_queue:
            self.__process_requests()
        self.set_state(State.IDLE)

        print(f"All requests have been fulfilled, elevator is now {self.get_state()}")

    def process_emergency(self) -> None:
        self.__passenger_up_queue.clear()
        self.__passenger_down_queue.clear()

        self.set_current_floor(1)
        self.set_state(State.IDLE)
        self.open_doors()
        self.set_emergency_status(True)

        print(f"Queues cleared, current floor is {self.get_current_floor()}. Door are {self.get_door_state()}")

    def add_up_request(self, request: Request) -> None:
        if request.get_origin() == RequestOrigin.OUTSIDE:
            pick_up_request = Request(request.get_origin(), request.get_origin_floor(), request.get_origin_floor())
            heapq.heappush(self.__passenger_up_queue, pick_up_request)
        heapq.heappush(self.__passenger_up_queue, request)

    def add_down_request(self, request: Request) -> None:
        if request.get_origin() == RequestOrigin.OUTSIDE:
            pick_up_request = Request(request.get_origin(), request.get_origin_floor(), request.get_origin_floor())
            self.__push_down_request(pick_up_request)
        self.__push_down_request(request)

    def __push_down_request(self, request: Request) -> None:
        heapq.heappush(self.__passenger_down_queue, (-request.get_destination_floor(), request))

    def __process_up_request(self) -> None:
        while self.__passenger_up_queue:
            up_request: Request = heapq.heappop(self.__passenger_up_queue)

            if self.get_current_floor() == up_request.get_destination_floor():
                print(f"Currently on floor {self.get_current_floor()}. No movement as destination is the same.")
                continue

            print (f"Current floor is {self.get_current_floor()}. Next stop: {up_request.get_destination_floor()}")

            try:
                print("Moving ", end = "")
                for _ in range(3):
                    print(". ", end = "", flush = True)
                    time.sleep(0.5)
            except KeyboardInterrupt:
                pass
            except Exception as e:
                print(f"Error: {e}")

            self.set_current_floor(up_request.get_destination_floor())
            print(f"Arrived at: {self.get_current_floor()}")

            self.open_doors()
            self.wait_for_seconds(3)
            self.close_doors()

        print("Finished processing all the up requests.")

    def __process_down_request(self) -> None:
        while self.__passenger_down_queue:
            _, down_request = heapq.heappop(self.__passenger_down_queue)

            if self.get_current_floor() == down_request.get_destination_floor():
                print(f"Currently on floor {self.get_current_floor()}. No movement as destination is the same.")
                continue
                
            print (f"Current floor is {self.get_current_floor()}. Next stop: {down_request.get_destination_floor()}")

            try:
                print("Moving ", end = "")
                for _ in range(3):
                    print(". ", end = "", flush = True)
                    time.sleep(0.5)
            except KeyboardInterrupt:
                pass
            except Exception as e:
                print(f"Error: {e}")

            self.set_current_floor(down_request.get_destination_floor())

            print(f"Arrived at: {self.get_current_floor()}")
            
            self.open_doors()
            self.wait_for_seconds(3)
            self.close_doors()

        print("Finished processing all the down requests.")

    def __process_requests(self) -> None:
        if self.get_state() == State.UP or self.get_state() == State.IDLE:
            self.__process_up_request()
            if self.__passenger_down_queue:
                print("Now processing down requests...")
                self.__process_down_request()
        else:
            self.__process_down_request()
            if self.__passenger_up_queue:
                print("Now processing up requests...")
                self.__process_up_request()