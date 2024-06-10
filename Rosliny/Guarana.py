import random
from Base.Roslina import Roslina


class Guarana(Roslina):
    def __init__(self, print_log, x=0, y=0, sila=0, wiek=0):
        super().__init__(x, y, 'G', "Guarana", sila, 0)
        self.wiek = wiek
        self.rozsiane = False
        self.print_log = print_log

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        rozsiew = random.randint(0, 24)
        self.rozsiane = rozsiew == 0

    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        off.setSila(off.getSila() + 3)
        self.print_log(f"{def_.getImie()} zostaje zjedzona przez {off.getImie()}"
                       f" i zwieksza jego sile o 3 pkt.\n Obecna sila {off.getImie()} wynosi {off.getSila()}")
        return off
