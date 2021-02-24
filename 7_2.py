from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def quantity(self):
        pass

    def __add__(self, other):
        return self.quantity + other.quantity

class Coat(Clothes):

    @property
    def quantity(self):
        return round(self.param / 6.5) + 0.5

class Costume(Clothes):
    @property
    def quantity(self):
        return (2 * self.param + 0.3) / 100


coat = Coat(42)
costume = Costume(48)
print(coat+costume)