import random
from Base.Roslina import Roslina
from Base.Zwierze import Zwierze


class Barszcz(Roslina):
    def __init__(self, print_log, x=0, y=0, sila=10, wiek=0):
        super().__init__(x, y, 'B', "Barszcz Sosnowskiego", sila, 0)
        self.wiek = wiek
        self.rozsiane = False
        self.print_log = print_log

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        self.eksterminacja(plansza, gra)
        rozsiew = random.randint(0, 49)
        self.rozsiane = rozsiew == 0

    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        if off.id == 'K':
            return off
        return def_

    def eksterminacja(self, plansza, gra):
        for i in range(len(gra)):
            org = gra[i]
            if (isinstance(org, Zwierze) and org.id != 'K') and \
                    ((org.getX() == self._x - 1 and org.getY() == self._y) or
                     (org.getX() == self._x + 1 and org.getY() == self._y) or
                     (org.getY() == self._y - 1 and org.getX() == self._x) or
                     (org.getY() == self._y + 1 and org.getX() == self._x)):
                self.print_log(f"{org.getImie()} umiera przez Barszcz Sosnowskiego")
                plansza[org.getX()][org.getY()] = None
                gra[i] = None
