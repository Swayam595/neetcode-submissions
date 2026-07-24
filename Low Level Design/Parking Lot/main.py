from parking_system import ParkingSystem
from parking_garage import ParkingGarage
from driver import Driver
from vehicle import Car, Truck, Limo
import uuid

def park_and_inform(driver: Driver, parking_system: ParkingSystem) -> None:
    driver_id = driver.get_driver_id()
    vehicle = driver.get_vehicle()
    
    print(f"Driver with {driver_id} ID is waiting to park their {vehicle.get_vehicle_type()}.")
    is_parked = parking_system.park_vehicle(driver)

    if is_parked:
        print(f"Driver with {driver_id} ID {vehicle.get_vehicle_type()} is parked.\n")
    else:
        print(f"Sorry! we do not have enough space to park you {vehicle.get_vehicle_type()}\n")

def remove_and_inform(driver: Driver, parking_system: ParkingSystem) -> None:
    try:
        parking_system.remove_vehicle(driver)
    except ValueError as ex:
        print(ex)  

parking_garage_floor_dimensions = [3, 2]
parking_garage_floor_count = len(parking_garage_floor_dimensions)

parking_garage = ParkingGarage().set_parking_floor_count(parking_garage_floor_count).set_floors_dimensions(parking_garage_floor_dimensions).build()

parking_system = ParkingSystem(parking_garage, 10)

driver1 = Driver(uuid.uuid4(), Car())
driver2 = Driver(uuid.uuid4(), Limo())
driver3 = Driver(uuid.uuid4(), Truck())

park_and_inform(driver1, parking_system)
park_and_inform(driver2, parking_system)
park_and_inform(driver3, parking_system)


remove_and_inform(driver3, parking_system)
remove_and_inform(driver1, parking_system)
remove_and_inform(driver2, parking_system)

park_and_inform(driver3, parking_system)
remove_and_inform(driver3, parking_system)