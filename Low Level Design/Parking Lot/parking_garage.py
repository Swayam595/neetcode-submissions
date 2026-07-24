from parking_floor import ParkingFloor
from vehicle import Vehicle

class ParkingGarage:
    __FLOOR_COUNT : int
    __FLOORS_DIMENSIONS: list[int]
    __PARKING_FLOORS: list[ParkingFloor]

    def __init__(self):
        self.__FLOOR_COUNT = 0
        self.__FLOORS_DIMENSIONS = []
        self.__PARKING_FLOORS = []

    def set_parking_floor_count(self, n) -> "ParkingGarage":
        self.__FLOOR_COUNT = n
        return self
    
    def get_parking_floor_count(self) -> int:
        return self.__FLOOR_COUNT
    
    def set_floors_dimensions(self, floor_dimensions: list[int]) -> "ParkingGarage":
        self.__FLOORS_DIMENSIONS = floor_dimensions
        return self
    
    def get_floors_dimensions(self) -> list[int]:
        return self.__FLOORS_DIMENSIONS
    
    def get_parking_floors(self) -> list[ParkingFloor]:
        return self.__PARKING_FLOORS
    
    def build(self) -> "ParkingGarage":
        self.__validate()
        self.__build_parking_floors()
        return self
    
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for floor in self.__PARKING_FLOORS:
            is_parked = floor.park_vehicle(vehicle)
            if is_parked:
                return True
        
        return False
    
    def remove_vehicle(self, vehicle: Vehicle):
        for floor in self.__PARKING_FLOORS:
            if floor.remove_vehicle(vehicle):
                return
    
    def __validate(self):
        if self.__FLOOR_COUNT == 0 or self.__FLOOR_COUNT != len(self.__FLOORS_DIMENSIONS):
            raise ValueError("Floor count and Floor dimensions must match")
    
    def __build_parking_floors(self):
        for i in range(self.__FLOOR_COUNT):
            dimension = self.__FLOORS_DIMENSIONS[i]
            parking_floor = ParkingFloor(dimension)
            self.__PARKING_FLOORS.append(parking_floor)