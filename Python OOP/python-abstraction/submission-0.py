class Superhero:
    def __init__(self, name: str):
       self._name = name
       self._power_level = 40
    
    def fly(self) -> str:
        message = ""
        if self._power_level >= 20:
            self._power_level -= 20
            message = "Up up and away!"
        else:
            message = "Too tired to fly..."
        
        return message

    
# Do not modify the code below
hero = Superhero("Superman")
print(hero.fly())  
print(hero.fly())
print(hero.fly())  
