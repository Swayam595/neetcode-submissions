class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts: int = 0
    total_balance: int = 0

    def __init__(self, name: str, balance: str) -> None:
        self.name = name
        self.balance = balance

        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance
    
    def print_account_balace(self):
        print(f"{self.name}'s balance: ${self.balance}")

    @classmethod
    def print_bank_details(cls):
        print(f"Total Accounts: {cls.total_accounts}")
        print(f"Total Balance: ${cls.total_balance}")

# TODO: Create two accounts
alices_account = BankAccount(name = "Alice", balance = 1000)
bobs_account = BankAccount(name = "Bob", balance = 2000)

# TODO: Print the information using the mentioned format
alices_account.print_account_balace()
bobs_account.print_account_balace()
BankAccount.print_bank_details()