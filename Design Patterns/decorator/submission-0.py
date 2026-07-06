class Coffee(ABC):
    @abstractmethod
    def getCost(self):
        pass

class SimpleCoffee(Coffee):
    def getCost(self):
        return 1.1

class CoffeeDecorator(Coffee):
    def __init__(self, decoratedCoffee):
        self.decoratedCoffee = decoratedCoffee

    def getCost(self):
        return self.decoratedCoffee.getCost()

class MilkDecorator(CoffeeDecorator):
    # Implement the Milk decorator
    def __init__(self, decoratedCoffee: Coffee):
        super().__init__(decoratedCoffee)
    
    def getCost(self):
        return self.decoratedCoffee.getCost() + 0.5

class SugarDecorator(CoffeeDecorator):
    # Implement the Sugar decorator
    def __init__(self, decoratedCoffee: Coffee):
        super().__init__(decoratedCoffee)
    
    def getCost(self):
        return self.decoratedCoffee.getCost() + 0.2

class CreamDecorator(CoffeeDecorator):
    # Implement the Cream decorator
    def __init__(self, decoratedCoffee: Coffee):
        super().__init__(decoratedCoffee)
    
    def getCost(self):
        return self.decoratedCoffee.getCost() + 0.7

