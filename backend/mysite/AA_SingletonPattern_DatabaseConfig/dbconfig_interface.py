from abc import ABC, abstractmethod

class InterfaceConfig(ABC):
    @abstractmethod
    def get_config(self):
        pass