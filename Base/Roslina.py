from abc import ABC, abstractmethod

from Base.Organizm import Organizm


class Roslina(Organizm, ABC):
    @abstractmethod
    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        pass

    @abstractmethod
    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        pass
    