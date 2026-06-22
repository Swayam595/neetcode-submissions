class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health


# TODO: Create Superhero instances

batman = SuperHero(name = "Batman", power = "Intelligence", health = 100)
superman = SuperHero(name = "Superman", power = "Strength", health = 150)

# TODO: Print out the attributes of each superhero
print (f"{batman.name}\n{batman.power}\n{batman.health}")
print (f"{superman.name}\n{superman.power}\n{superman.health}")