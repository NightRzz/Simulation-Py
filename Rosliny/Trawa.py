import random
from Base.Roslina import Roslina


class Trawa(Roslina):
    def __init__(self, x=0, y=0, sila=0, wiek=0):
        super().__init__(x, y, 'T', "Trawa", sila, 0)
        self.wiek = wiek
        self.rozsiane = False

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        rozsiew = random.randint(0, 7)
        self.rozsiane = rozsiew == 0

    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        return off
