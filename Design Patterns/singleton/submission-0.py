import threading

class Singleton:
    __instance_lock = threading.Lock()
    __unique_instance: None | Singleton = None
    __value: str

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls.__unique_instance is None:
            with cls.__instance_lock:
                if cls.__unique_instance is None:
                    cls.__unique_instance = super(Singleton, cls).__new__(cls)
                    cls.__unique_instance.setValue("")

        return cls.__unique_instance

    def getValue(self) -> str:
        return self.__value

    def setValue(self, value: str):
        self.__value = value