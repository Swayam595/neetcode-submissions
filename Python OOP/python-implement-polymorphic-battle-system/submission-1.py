class Hero:
    def __init__(self, name: str, power: int):
        self.name = name
        self.health = 100
        self.power = power
    
    def attack(self) -> int:
        return self.power

# TODO: Implement the Warrior and Mage classes
# TODO: Implement the battle function
class Warrior(Hero):
    def __init__(self, name: str, power: str):
        super().__init__(name, power)
        
    def attack(self) -> int:
        return self.power + 10

class Mage(Hero):
    def __init__(self, name: str, power: str):
        super().__init__(name, power)
        self.health = 80
    
    def attack(self) -> int:
        return self.power + 20

def show_attack(hero: Hero) -> None:
    print(f"{hero.name} attacks with {hero.attack()} damage!") 


# Do not modify the following code
warrior = Warrior("Bob", 20)
mage = Mage("Alice", 15)

show_attack(warrior)  
show_attack(mage)    
