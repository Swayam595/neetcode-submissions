import uuid 

class BankTeller:
    def __init__(self, employee_id: uuid):
        self.__employee_id = employee_id

    def get_employee_id(self) -> uuid:
        return self.__employee_id