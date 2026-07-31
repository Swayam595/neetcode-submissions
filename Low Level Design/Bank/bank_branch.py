import random
import uuid
from bank_system import BankSystem
from bank_teller import BankTeller

class BankBranch:
    def __init__(self, address: str, cash_on_hand: int, bank_system: BankSystem):
        self.__address = address
        self.__cash_on_hand = cash_on_hand
        self.__bank_system = bank_system
        self.__tellers = []

    def add_teller(self, teller: BankTeller) -> None:
        self.__tellers.append(teller)

    def open_account(self, customer_name: str) -> uuid:
        self.__validate_tellers_present()

        teller = self.__get_available_teller()
        return self.__bank_system.open_account(customer_name, teller.get_employee_id())

    def deposit(self, customer_id: uuid, amount: int) -> None:
        self.__validate_tellers_present()

        teller = self.__get_available_teller()
        self.__bank_system.deposit(customer_id, teller.get_employee_id(), amount)

    def withdraw(self, customer_id: uuid, amount: int) -> None:
        self.__validate_banks_adequate_cash_available(amount)
        self.__validate_tellers_present()

        teller = self.__get_available_teller()
        self.__bank_system.withdraw(customer_id, teller.get_employee_id(), amount)
        self.__cash_on_hand -= amount

    def collect_cash(self, ratio: int) -> int:
        cash_to_collect = round(self.__cash_on_hand * ratio)
        self.__cash_on_hand -= cash_to_collect
        return cash_to_collect

    def provide_cash(self, amount: int) -> None:
        self.__cash_on_hand += amount

    def __get_available_teller(self) -> BankTeller:
        index = round(random.random() * (len(self.__tellers) - 1))
        return self.__tellers[index]

    def __validate_tellers_present(self) -> None:
        if len(self.__tellers) == 0:
            raise ValueError("Bank does not have any tellers")

    def __validate_banks_adequate_cash_available(self, amount: int) -> None:
        if amount > self.__cash_on_hand:
            raise ValueError("Cash shortage in bank.")