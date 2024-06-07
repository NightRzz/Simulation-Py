from Base.Organizm import Organizm
from abc import ABC, abstractmethod


class Zwierze(Organizm, ABC):
    @abstractmethod
    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        pass

    @abstractmethod
    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        pass
