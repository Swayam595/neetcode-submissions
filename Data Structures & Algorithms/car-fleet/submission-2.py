class Solution:
    # TC -> O(N * log(N))
    # SC -> O(N) for creating cars array
    # N -> # of cars
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]
        cars.sort(key = lambda x: x[0], reverse = True)

        return self.__car_fleet_stack(target, cars)

    def __car_fleet_stack(self, target: int, cars: List[List[int]]) -> int:
        stack = []
        fleet = 0
        n = len(cars)        

        for i in range(n):
            car_position = cars[i][0]
            car_speed = cars[i][1]
            take_take_by_car_to_reach_target = (target - car_position) / car_speed

            stack.append(take_take_by_car_to_reach_target)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)