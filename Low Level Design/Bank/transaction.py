from abc import ABC, abstractmethod
import uuid

class Transaction(ABC):
    def __init__(self, customer_id: uuid, teller_id: uuid):
        self.__customer_id = customer_id
        self.__teller_id = teller_id

    def get_customer_id(self) -> uuid:
        return self.__customer_id

    def get_teller_id(self) -> uuid:
        return self.__teller_id

    @abstractmethod
    def get_transaction_details(self) -> str:
        pass

class Deposit(Transaction):
    def __init__(self, customer_id: uuid, teller_id: uuid, amount: int = 0):
        super().__init__(customer_id, teller_id)
        self.__amount = amount

    def get_transaction_details(self):
        return f"Teller {self.get_teller_id()} deposited {self.__amount} for the customer with Id {self.get_customer_id()}"

class Withdraw(Transaction):
    def __init__(self, customer_id: uuid, teller_id: uuid, amount: int = 0):
            super().__init__(customer_id, teller_id)
            self.__amount = amount

    def get_transaction_details(self):
        return f"Teller {self.get_teller_id()} withdrew {self.__amount} for the customer with Id {self.get_customer_id()}"

class OpenAccount(Transaction):
    def __init__(self, customer_id: uuid, teller_id: uuid):
        super().__init__(customer_id, teller_id)

    def get_transaction_details(self):
        return f"Teller {self.get_teller_id()} opened an account for the customer with Id {self.get_customer_id()}"