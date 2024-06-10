import random
from Base.Roslina import Roslina


class Mlecz(Roslina):
    def __init__(self, print_log, x=0, y=0, sila=0, wiek=0):
        super().__init__(x, y, 'M', "Mlecz", sila, 0)
        self.wiek = wiek
        self.rozsiane = False
        self.print_log = print_log

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        self.rozsiane = False
        for _ in range(3):
            rozsiew = random.randint(0, 7)
            if rozsiew == 0:
                self.rozsiane = True
                break

    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        return off
