import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, *args: float) -> float:
        if len(args) == 1:
            radius = args[0]
            area = math.pi * pow(radius, 2)
        elif len(args) == 2:
            length = args[0]
            breadth = args[1]
            area = length * breadth
        else:
            raise ValueError("Provide at most 2 arguments")
        
        return round(area, 2)
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
