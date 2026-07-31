import uuid

class BankAccount:
    def __init__(self, customer_id: uuid, name: str, balance: int = 0):
        self.__customer_id = customer_id
        self.__name = name
        self.__balance = balance

    def get_balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> None:
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        if amount > self.__balance:
            raise ValueError("Insufficient Balance in the account.")
        self.__balance -= amount

    def get_customer_id(self) -> uuid:
        return self.__customer_id

    def get_customer_name(self) -> str:
        return self.__name