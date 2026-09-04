class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]
        cars.sort(key = lambda x: x[0], reverse = True)

        # return self.__car_fleet_stack(target, cars)
        return self.__car_fleet_iteration(target, cars)

    def __car_fleet_iteration(self, target: int, cars: List[List[int]]) -> int:
        prev_time = self.__compute_time_taken(target, cars[0][0], cars[0][1])
        fleets = 1

        for i in range(1, len(cars)):
            car_position = cars[i][0]
            car_speed = cars[i][1]
            curr_time_taken = self.__compute_time_taken(target, car_position, car_speed)

            if curr_time_taken > prev_time:
                fleets += 1
                prev_time = curr_time_taken
        
        return fleets

    # TC -> O(N * log(N))
    # SC -> O(N) for creating cars array
    # N -> # of cars
    def __car_fleet_stack(self, target: int, cars: List[List[int]]) -> int:
        stack = []
        n = len(cars)        

        for i in range(n):
            car_position = cars[i][0]
            car_speed = cars[i][1]
            take_take_by_car_to_reach_target = self.__compute_time_taken(target, car_position, car_speed)

            stack.append(take_take_by_car_to_reach_target)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
    
    def __compute_time_taken(self, target: int, poition: int, speed: int) -> float:
        return (target - poition) / speed