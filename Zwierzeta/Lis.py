import random
from Base.Zwierze import Zwierze


class Lis(Zwierze):
    def __init__(self, print_log, x=0, y=0, sila=3, wiek=0):
        super().__init__(x, y, 'L', "Lis", sila, 7)
        self.wiek = wiek
        self.print_log = print_log

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        kierunek = random.randint(0, 3)
        if kierunek == 0 and self._y > 0:
            if isinstance(plansza[self._x][self._y - 1], Zwierze) and (plansza[self._x][self._y - 1].getSila() < self._sila or plansza[self._x][self._y - 1].id == 'L'):
                self._y -= 1
            else:
                self._y -= 1
        elif kierunek == 1 and self._y < szerokosc - 1:
            if isinstance(plansza[self._x][self._y + 1], Zwierze) and (plansza[self._x][self._y + 1].getSila() < self._sila or plansza[self._x][self._y + 1].id == 'L'):
                self._y += 1
            else:
                self._y += 1
        elif kierunek == 2 and self._x < wysokosc - 1:
            if isinstance(plansza[self._x + 1][self._y], Zwierze) and (plansza[self._x + 1][self._y].getSila() < self._sila or plansza[self._x + 1][self._y].id == 'L'):
                self._x += 1
            else:
                self._x += 1
        elif kierunek == 3 and self._x > 0:
            if isinstance(plansza[self._x - 1][self._y], Zwierze) and (plansza[self._x - 1][self._y].getSila() < self._sila or plansza[self._x - 1][self._y].id == 'L'):
                self._x -= 1
            else:
                self._x -= 1

    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        if def_.id == off.id:
            self.rozmnoz = True
            return def_
        elif def_.id == self.id:  # broni
            if def_.getSila() > off.getSila():
                self.print_log(f"{def_.getImie()} wygrywa z {off.getImie()}")
                return def_
            elif def_.getSila() == off.getSila():
                self.print_log(f"{off.getImie()} wygrywa z {def_.getImie()}")
                return off
            else:
                self.print_log(f"{def_.getImie()} przegrywa z {off.getImie()}")
                return off
        elif off.id == self.id:  # atakuje
            if off.getSila() > def_.getSila():
                if off == def_.kolizja(off, def_, plansza, szerokosc, wysokosc):
                    self.print_log(f"{off.getImie()} wygrywa z {def_.getImie()}")
                    return off
                elif def_.zolwodparlatak:
                    return def_
            elif off.getSila() == def_.getSila():
                self.print_log(f"{off.getImie()} wygrywa z {def_.getImie()}")
                return off
            else:
                self.print_log(f"{off.getImie()} przegrywa z {def_.getImie()}")
                return def_
        return def_
