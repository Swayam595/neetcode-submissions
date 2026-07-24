
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_size: int):
        self.__vehicle_size = vehicle_size

    def get_vehicle_size(self) -> int:
        return self.__vehicle_size
    
    @abstractmethod
    def get_vehicle_type(self) -> str:
        pass
    
class Car(Vehicle):
    def __init__(self):
        super().__init__(1)
    
    def get_vehicle_type(self) -> str:
        return "Car"

class Limo(Vehicle):
    def __init__(self):
        super().__init__(2)
    
    def get_vehicle_type(self) -> str:
        return "Limo"

class Truck(Vehicle):
    def __init__(self):
        super().__init__(3)

    def get_vehicle_type(self) -> str:
        return "Truck"