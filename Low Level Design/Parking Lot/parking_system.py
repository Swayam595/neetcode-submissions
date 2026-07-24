import datetime
import math
from parking_garage import ParkingGarage
from driver import Driver

class ParkingSystem:
    def __init__(self, parking_garage: ParkingGarage, hourly_rate: int):
        self.__parking_garage = parking_garage
        self.__hourly_rate = hourly_rate
        self.__time_parked = dict()

    def park_vehicle(self, driver: Driver) -> bool:
        entry_time = datetime.datetime.now().hour

        vehicle = driver.get_vehicle()
        isParked = self.__parking_garage.park_vehicle(vehicle)

        if isParked:
            self.__time_parked[driver.get_driver_id()] = entry_time
        
        return isParked
    
    def remove_vehicle(self, driver: Driver) -> None:
        if driver.get_driver_id() not in self.__time_parked:
            raise ValueError("Your vehicle is not parked in our garage")

        vehicle = driver.get_vehicle()

        entry_time = self.__time_parked[driver.get_driver_id()]
        exit_time = datetime.datetime.now().hour
        time_parked = math.ceil(exit_time - entry_time)

        parking_cost = vehicle.get_vehicle_size() * time_parked * self.__hourly_rate

        driver.charge(parking_cost)
        del self.__time_parked[driver.get_driver_id()]

        self.__parking_garage.remove_vehicle(vehicle)

        return
