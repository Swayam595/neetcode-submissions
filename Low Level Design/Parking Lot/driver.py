from vehicle import Vehicle
import uuid

class Driver:
    def __init__(self, id: uuid, vehicle: Vehicle):
        self.__id = id
        self.__vehicle = vehicle
        self.__payment_due = 0

    def get_driver_id(self) -> uuid:
        return self.__id
    
    def get_vehicle(self) -> Vehicle:
        return self.__vehicle
    
    def charge(self, amount: int):
        self.__payment_due += amount
