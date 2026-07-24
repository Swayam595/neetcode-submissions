from vehicle import Vehicle

class ParkingFloor:
    def __init__(self, spots_count: int):
        self.__spots = [0] * spots_count
        self.__vehicle_map = dict()

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        vehicle_size = vehicle.get_vehicle_size()

        l = 0
        r = 0

        while r < len(self.__spots):
            if self.__spots[r] != 0:
                l = r + 1
            
            if r - l + 1 == vehicle_size and self.__has_enough_space(l, r):
                for i in range(l, r + 1):
                    self.__spots[i] = 1
                self.__vehicle_map[vehicle] = [l, r]
                return True

            r += 1
            
        return False
    
    def remove_vehicle(self, vehicle: Vehicle) -> bool:
        l, r = self.__vehicle_map.get(vehicle, [-1, -1])

        if l == -1:
            print("Vehicle not found on this floor")
        
        for i in range(l, r + 1):
            self.__spots[i] = 0

        del self.__vehicle_map[vehicle]
        print("Vehicle Removed")
        return True
    
    def get_parking_spots(self) -> list:
        return self.__spots
    
    def get_vehicle_spots(self, vehicle: Vehicle) -> list:
        if vehicle not in self.__vehicle_map:
            raise ValueError("Vehicle Not Found")
        
        return self.__vehicle_map[vehicle]
    
    def __has_enough_space(self, l: int, r: int) -> bool:
        for i in range(l, r + 1):
            if self.__spots[i] != 0:
                return False
        return True
