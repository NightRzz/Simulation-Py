import random
from Base.Roslina import Roslina


class WilczeJagody(Roslina):
    def __init__(self, print_log, x=0, y=0, sila=99, wiek=0):
        super().__init__(x, y, 'J', "Wilcze Jagody", sila, 0)
        self.wiek = wiek
        self.rozsiane = False
        self.print_log = print_log

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        rozsiew = random.randint(0, 29)
        self.rozsiane = rozsiew == 0

    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        self.print_log(f"{off.getImie()} zjada {def_.getImie()} i ginie")
        return def_
