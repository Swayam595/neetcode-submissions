class SuperHero:
    def __init__(self, name: str, health: int, power_level: int):
        self.name = name
        # TODO: Add the private attributes
        self.__health = health
        self.__power_level = power_level
    
    # TODO: Add the getter and setter methods

    #Getter
    @property
    def health(self) -> int:
        return self.__health
    
    @property
    def power_level(self) -> int:
        return self.__power_level

    def get_health(self) -> int:
        return self.health
    
    def get_power_level(self) -> int:
        return self.power_level
    
    # Setter
    @health.setter
    def health(self, new_health: int) -> None:
        if 0 <= new_health <= 100:
            self.__health = new_health
        elif new_health > 100:
            print("You can't set the health to more than 100")
        else:
            print("You can't set the health to less than 0")
        
    @power_level.setter
    def power_level(self, new_power_level: int) -> None:
        if 1 <= new_power_level <= 10:
            self.__power_level = new_power_level
        elif new_power_level < 1:
            print("You can't set the power level to less than 1")
        else:
            print("You can't set the power level to more than 10")

    def set_health(self, new_health: int) -> None:
        self.health = new_health
    
    def set_power_level(self, new_power_level: int) -> None:
        self.power_level = new_power_level

    




super_hero = SuperHero("Batman", 80, 9)

print(super_hero.get_health()) # this should print 80
super_hero.set_health(110) # this should print You can't set the health to more than 100
super_hero.set_health(-10) # this should print You can't set the health to less than 100
super_hero.set_health(70)

print(super_hero.get_power_level()) # this should print 9
super_hero.set_power_level(11) # this should print You can't set the power level to more than 10
super_hero.set_power_level(0) # this should print You can't set the power level to less than 1
super_hero.set_power_level(7)



# TODO: print the hero's attributes
print (f"{super_hero.name} has {super_hero.health} health and {super_hero.power_level} power level")
