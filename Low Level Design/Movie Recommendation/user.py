from uuid import uuid4, UUID

class User:
    def __init__(self, name: str):
        self.__name = name
        self.__id = uuid4()

    def get_id(self) -> UUID:
        return self.__id

    def get_name(self) -> str:
        return self.__name