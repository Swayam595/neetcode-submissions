from bank_branch import BankBranch
from bank_system import BankSystem


class BankHQ:
    def __init__(self, branches: list[BankBranch], bank_system: BankSystem, total_cash: int):
        self.__branches = branches
        self.__bank_system = bank_system
        self.__total_cash = total_cash

    def add_branch(self, address: str, initial_funds: int) -> BankBranch:
        branch = BankBranch(address, initial_funds, self.__bank_system)
        self.__branches.append(branch)
        return branch

    def collect_cash(self, ratio: float) -> None:
        for branch in self.__branches:
            cash_collected = branch.collect_cash(ratio)
            self.__total_cash += cash_collected

    def print_transactions(self) -> None:
        for transaction in self.__bank_system.get_transactions():
            print(transaction.get_transaction_details())