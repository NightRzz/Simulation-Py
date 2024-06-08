import random
from Base.Roslina import Roslina
from Base.Zwierze import Zwierze


class Barszcz(Roslina):
    def __init__(self,print_log, x=0, y=0, sila=10, wiek=0):
        super().__init__(x, y, 'B', "Barszcz Sosnowskiego", sila, 0)
        self.wiek = wiek
        self.rozsiane = False
        self.print_log = print_log

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        self.eksterminacja(plansza, gra)
        rozsiew = random.randint(0, 49)
        self.rozsiane = rozsiew == 0

    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        return def_

    def eksterminacja(self, plansza, gra):
        for i in range(len(gra)):
            org = gra[i]
            if (isinstance(org, Zwierze) or org is not None and org.id == 'C') and \
                    ((org.x == self.x - 1 and org.y == self.y) or
                     (org.x == self.x + 1 and org.y == self.y) or
                     (org.y == self.y - 1 and org.x == self.x) or
                     (org.y == self.y + 1 and org.x == self.x)):
                self.print_log(f"{org.imie} umiera przez Barszcz Sosnowskiego")
                plansza[org.x][org.y] = None
                gra[i] = None
