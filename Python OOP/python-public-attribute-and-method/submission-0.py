class StoreItem:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
    
    def print(self):
        print(f"{self.name}\n{self.price}")


chips = StoreItem("Chips", 1.99) # Don't modify this line

# TODO: Access the attributes of the chips object and display them
chips.print()


