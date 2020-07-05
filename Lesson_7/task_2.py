from abc import ABC, abstractmethod


class Textil(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def get_consum(self):
        pass

    def __add__(self, other):
        return self.get_consum + other.get_consum


class Coat(Textil):
    @property
    def get_consum(self):
        coat_cons = round(self.param / 6.5 + 0.5)
        print(f"Расход ткани для пальто: {coat_cons}")
        return coat_cons


class Suit(Textil):
    @property
    def get_consum(self):
        suit_cons = round(self.param * 2 + 0.3)
        print(f"Расход ткани для костюма: {suit_cons}")
        return suit_cons


coat = Coat(50)
suit = Suit(1.7)
print(coat + suit)

