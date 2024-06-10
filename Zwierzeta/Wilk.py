import random
from Base.Zwierze import Zwierze


class Wilk(Zwierze):
    def __init__(self, print_log, x=0, y=0, sila=9, wiek=0):
        super().__init__(x, y, 'W', "Wilk", sila, 5)
        self.wiek = wiek
        self.print_log = print_log

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        kierunek = random.randint(0, 3)
        if kierunek == 0 and self._y > 0:
            self._y -= 1
        elif kierunek == 1 and self._y < szerokosc - 1:
            self._y += 1
        elif kierunek == 2 and self._x < wysokosc - 1:
            self._x += 1
        elif kierunek == 3 and self._x > 0:
            self._x -= 1

    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        if def_.id == off.id:
            def_.rozmnoz = True
            return def_
        elif def_.id == self.id:  # broni
            if def_.getSila() > off.getSila():
                self.print_log(f"{def_.getImie()} wygrywa z {off.getImie()}")
                return def_
            else:
                self.print_log(f"{def_.getImie()} przegrywa z {off.getImie()}")
                return off
        elif off.id == self.id:  # atakuje
            if off.getSila() > def_.getSila():
                if off == def_.kolizja(off, def_, plansza, szerokosc, wysokosc):
                    self.print_log(f"{off.getImie()} wygrywa z {def_.getImie()}")
                    return off
            elif off.getSila() == def_.getSila():
                self.print_log(f"{off.getImie()} wygrywa z {def_.getImie()}")
                return off
            else:
                self.print_log(f"{off.getImie()} przegrywa z {def_.getImie()}")
                return def_
        return None
