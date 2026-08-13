from enums import ElevatorType
from elevator import Elevator
from passenger_elevator import PassengerElevator
from service_elevator import ServiceElevator

class ElevatorFactory:
    @staticmethod
    def create_elevator(elevator_type: ElevatorType) -> Elevator:
        if elevator_type == ElevatorType.PASSENGER:
            return PassengerElevator(1, False)
        elif elevator_type == ElevatorType.SERVICE:
            return ServiceElevator(1, False)
        else:
            return None