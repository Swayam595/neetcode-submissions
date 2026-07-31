import uuid
from bank_account import BankAccount
from transaction import OpenAccount, Deposit, Withdraw

class BankSystem:
    def __init__(self, accounts: dict, transactions: list):
        self.__accounts = accounts
        self.__transactions = transactions

    def get_accounts(self) -> list:
        return self.__accounts

    def get_account(self, customer_id: uuid) -> BankAccount:
        if customer_id not in self.__accounts:
            raise ValueError(f"There is no customer with the Id {customer_id}")
        return self.__accounts[customer_id]

    def get_transactions(self) -> list:
        return self.__transactions

    def open_account(self, customer_name: str, teller_id: uuid) -> uuid:
        customer_id = uuid.uuid4()
        account = BankAccount(customer_id=customer_id, name=customer_name)

        transaction = OpenAccount(customer_id, teller_id)
        self.__transactions.append(transaction)

        self.__accounts[customer_id] = account

        return customer_id

    def deposit(self, customer_id: uuid, teller_id: uuid, amount: int) -> None:
        account = self.get_account(customer_id)
        account.deposit(amount)
        transaction = Deposit(customer_id, teller_id, amount)
        self.__transactions.append(transaction)

    def withdraw(self, customer_id: uuid, teller_id: uuid, amount: int) -> int:
        account = self.get_account(customer_id)
        account.withdraw(amount)

        transaction = Withdraw(customer_id, teller_id, amount)
        self.__transactions.append(transaction)