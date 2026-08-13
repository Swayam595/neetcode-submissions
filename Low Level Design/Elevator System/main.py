from elevator_factory import ElevatorFactory
from controller import Controller
from request import Request
from service_request import ServiceRequest
from enums import RequestOrigin

class Main:
    @staticmethod
    def main():
        factory = ElevatorFactory()
        controller = Controller(factory)

        controller.send_passenger_up_requests(Request(RequestOrigin.OUTSIDE, 1, 5))

        controller.send_passenger_down_requests(Request(RequestOrigin.OUTSIDE, 4, 2))

        controller.send_passenger_up_requests(Request(RequestOrigin.OUTSIDE, 3, 6))

        controller.handle_passenger_requests()

        controller.send_passenger_up_requests(Request(RequestOrigin.OUTSIDE, 1, 9))

        controller.send_passenger_down_requests(Request(RequestOrigin.INSIDE, 5))

        controller.send_passenger_up_requests(Request(RequestOrigin.OUTSIDE, 4, 12))

        controller.send_passenger_down_requests(Request(RequestOrigin.OUTSIDE, 10, 2))

        controller.handle_passenger_requests()

        print("Now processing service requests")

        controller.send_service_request_requests(ServiceRequest(RequestOrigin.INSIDE, 13))

        controller.send_service_request_requests(ServiceRequest(RequestOrigin.OUTSIDE, 13, 2))

        controller.send_service_request_requests(ServiceRequest(RequestOrigin.INSIDE, 13, 15))

        controller.handle_service_requests()

if __name__ == "__main__":
    Main.main()