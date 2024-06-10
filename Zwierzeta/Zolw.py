import random
from Base.Zwierze import Zwierze


class Zolw(Zwierze):
    def __init__(self, print_log, x=0, y=0, sila=2, wiek=0):
        super().__init__(x, y, 'Z', "Zolw", sila, 1)
        self.wiek = wiek
        self.zolwodparlatak = False
        self.print_log = print_log

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        ruch = random.randint(0, 2)
        if ruch == 0:
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
            if off.getSila() < 5:  # odparcie ataku
                self.print_log(f"{def_.getImie()} odpiera atak {off.getImie()}")
                self.zolwodparlatak = True
                return def_
            else:
                if def_.getSila() > off.getSila():
                    self.print_log(f"{def_.getImie()} wygyrwa z {off.getImie()}")
                    return def_
                else:
                    self.print_log(f"{def_.getImie()} przegrywa z {off.getImie()}")
                    return off
        elif off.id == self.id:  # atakuje
            if off.getSila() > def_.getSila():
                if off == def_.kolizja(off, def_, plansza, szerokosc, wysokosc):
                    self.print_log(f"{off.getImie()} wygyrwa z {def_.getImie()}")
                    return off
            elif off.getSila() == def_.getSila():
                self.print_log(f"{off.getImie()} wygrywa z {def_.getImie()}")
                return off
            else:
                self.print_log(f"{off.getImie()} przegrywa z {def_.getImie()}")
                return def_
        return None
