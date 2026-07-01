class Meal:
    def __init__(self):
        self.cost = 0.0
        self.takeOut = False
        self.main = ""
        self.drink = ""

    def getCost(self) -> float:
        return self.cost

    def setCost(self, cost: float) -> None:
        self.cost = cost

    def getTakeOut(self) -> bool:
        return self.takeOut

    def setTakeOut(self, takeOut: bool) -> None:
        self.takeOut = takeOut

    def getMain(self) -> str:
        return self.main

    def setMain(self, main: str) -> None:
        self.main = main

    def getDrink(self) -> str:
        return self.drink

    def setDrink(self, drink: str) -> None:
        self.drink = drink


class MealBuilder:
    
    def __init__(self):
        self.__meal = Meal()

    def addCost(self, cost: float) -> 'MealBuilder':
        self.__meal.setCost(cost)
        return self

    def addTakeOut(self, takeOut: bool) -> 'MealBuilder':
        self.__meal.setTakeOut(takeOut)
        return self

    def addMainCourse(self, main: str) -> 'MealBuilder':
        self.__meal.setMain(main)
        return self

    def addDrink(self, drink: str) -> 'MealBuilder':
        self.__meal.setDrink(drink)
        return self

    def build(self) -> Meal:
        self.__validateMeal()
        return self.__meal
    
    def __validateMeal(self) -> bool:
        if self.__meal.getCost() <= 0:
            raise ValueError("Const of the meal must be greater than 0")

        if self.__meal.getMain() == "":
            raise ValueError("Invalid Meal was provided")
            

