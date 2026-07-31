import uuid
from bank_hq import BankHQ
from bank_system import BankSystem
from bank_teller import BankTeller
from bank_branch import BankBranch


bank_system = BankSystem(accounts=dict(), transactions=list())
bank = BankHQ(branches=list(), bank_system=bank_system, total_cash=20000)

branch1 = bank.add_branch(address="Balewadi", initial_funds=2000)
branch2 = bank.add_branch(address="BBSR", initial_funds=2000)
branch3 = bank.add_branch(address="Puri", initial_funds=2000)
branch4 = bank.add_branch(address="SBP", initial_funds=2000)
branch5 = bank.add_branch(address="Pune", initial_funds=2000)

branches = [branch1, branch2, branch3, branch4, branch5]

for branch in branches:
    for _ in range(3):
        teller = BankTeller(employee_id=uuid.uuid4())
        branch.add_teller(teller=teller)

customer_id_1 = branch1.open_account("Ravi")
customer_id_2 = branch1.open_account("Ram")
customer_id_3 = branch1.open_account("x1")
customer_id_4 = branch1.open_account("x2")
customer_id_5 = branch1.open_account("x3")

customer_id_6 = branch2.open_account("b2")
customer_id_7 = branch3.open_account("b3")
customer_id_8 = branch4.open_account("b4")
customer_id_9 = branch5.open_account("b5")
customer_id_10 = branch1.open_account("b1")

branch1.deposit(customer_id=customer_id_1, amount=2000)
branch1.deposit(customer_id=customer_id_2, amount=2000)
branch1.deposit(customer_id=customer_id_3, amount=2000)
branch1.deposit(customer_id=customer_id_4, amount=2000)
branch1.deposit(customer_id=customer_id_5, amount=2000)

branch1.withdraw(customer_id=customer_id_5, amount=500)


bank.print_transactions()