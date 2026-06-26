class SpiderMan:
    def attack(self) -> str:
        return "Web Shooter!"
    
    def defend(self) -> str:
        return "Spider Sense!"

# TODO: Create the BlackWidow class with attack() and defend() methods
class BlackWidow:
    def attack(self) -> str:
        return "Widow's Bite!"
    
    def defend(self) -> str:
        return "Acrobatic Dodge!"

# TODO: Create the battle_sequence() function
def battle_sequence(hero) -> None:
    print(hero.attack())
    print(hero.defend())


# Don't modify the code below
spider_man = SpiderMan()
black_widow = BlackWidow()

battle_sequence(spider_man)
battle_sequence(black_widow)
