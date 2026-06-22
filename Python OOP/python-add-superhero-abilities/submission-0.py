class SuperHero:
    """
    A class to represent a superhero.
    
    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """
    
    def __init__(self, name: str, power: str, health: int):
        """Initialises the SuperHero class with provided class attributes"""
        self.name = name
        self.power = power
        self.health = health
    

    # TODO: Define attack method and implement it
    def attack(self):
        """Prints the SuperHero's name and SuperHero's attacl power"""
        print(f"{self.name} attacks with {self.power}!")

    # TODO: Define heal method and implment it
    def heal(self):
        """Increases the SuperHero's health by 10 and prints the new health"""
        self.health += 10
        print(f"{self.name} heals 10 points. New health: {self.health}.")

# TODO: Create superhero instance
catwoman = SuperHero(name = "Catwoman", power = "Agility", health = 120)

# TODO: Use the attack() and heal() method
catwoman.attack()
catwoman.heal()
