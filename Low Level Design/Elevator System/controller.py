from enums import ElevatorType
from passenger_elevator import PassengerElevator
from service_elevator import ServiceElevator
from elevator_factory import ElevatorFactory
from request import Request

class Controller:
    def __init__(self, factory: ElevatorFactory):
        self.__factory: ElevatorFactory = factory
        self.__passenger_elevator: PassengerElevator = self.__factory.create_elevator(ElevatorType.PASSENGER)
        self.__service_elevator: ServiceElevator = self.__factory.create_elevator(ElevatorType.SERVICE)

    def send_passenger_up_requests(self, request: Request) -> None:
        self.__passenger_elevator.add_up_request(request)

    def send_passenger_down_requests(self, request: Request) -> None:
        self.__passenger_elevator.add_down_request(request)

    def send_service_request_requests(self, request: Request) -> None:
        self.__service_elevator.add_request_to_queue(request)

    def handle_passenger_requests(self) -> None:
        self.__passenger_elevator.operate()

    def handle_service_requests(self) -> None:
        self.__service_elevator.operate()

    def handle_emergency(self):
        self.__passenger_elevator.process_emergency()
        self.__service_elevator.process_emergency()