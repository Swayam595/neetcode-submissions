from suite import Suite

class Card:
    def __init__(self, suite: Suite, value: int):
        self.__suite = suite
        self.__value = value
    
    def get_suite(self) -> Suite:
        return self.__suite

    def get_value(self) -> int:
        return self.__value
    
    def print(self) -> None:
        print (f"{self.__suite} -> {self.__value}")