from abc import ABC, abstractmethod

class OrderStates(ABC):
    @abstractmethod
    def create(self, user, order_id, isbn, quantity):
        pass

    @abstractmethod
    def advance(self, order):
        pass

    @abstractmethod
    def cancel(self, order):
        pass