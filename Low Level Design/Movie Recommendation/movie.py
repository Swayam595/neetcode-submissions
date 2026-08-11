from uuid import uuid4, UUID

class Movie:
    def __init__(self, title: str):
        self.__id = uuid4()
        self.__title = title

    def get_id(self) -> UUID:
        return self.__id

    def get_title(self) -> str:
        return self.__title