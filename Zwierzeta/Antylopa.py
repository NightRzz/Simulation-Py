import random
from Base.Zwierze import Zwierze


class Antylopa(Zwierze):
    def __init__(self, print_log, x=0, y=0, sila=4, wiek=0):
        super().__init__(x, y, 'A', "Antylopa", sila, 4)
        self.wiek = wiek
        self.print_log = print_log

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        kierunek = random.randint(0, 3)
        if kierunek == 0 and self._y > 1:
            self._y -= 2
        elif kierunek == 1 and self._y < szerokosc - 2:
            self._y += 2
        elif kierunek == 2 and self._x < wysokosc - 2:
            self._x += 2
        elif kierunek == 3 and self._x > 1:
            self._x -= 2

    def ucieka_def(self, plansza, off, def_):
        plansza[self._x][self._y] = def_
        self.print_log(f"{self.getImie()} ucieka przed {off.getImie()} na pole {self._x} {self._y}")
        return off

    def ucieka_off(self, plansza, off, def_):
        plansza[self._x][self._y] = off
        self.print_log(f"{self.getImie()} ucieka przed {def_.getImie()} na pole {self._x} {self._y}")
        return def_

    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        ucieczka = random.randint(0, 1)
        if def_.id == off.id:
            self.rozmnoz = True
            return off
        elif ucieczka == 1 and isinstance(def_, Zwierze):
            kierunek = random.randint(0, 3)
            if kierunek == 0 and self._y > 0 and plansza[self._x][self._y - 1] is None:
                self._y -= 1
                return self.ucieka_def(plansza, off, def_) if def_.id == self.id else self.ucieka_off(plansza, off, def_)
            elif kierunek == 1 and self._y < szerokosc - 1 and plansza[self._x][self._y + 1] is None:
                self._y += 1
                return self.ucieka_def(plansza, off, def_) if def_.id == self.id else self.ucieka_off(plansza, off, def_)
            elif kierunek == 2 and self._x < wysokosc - 1 and plansza[self._x + 1][self._y] is None:
                self._x += 1
                return self.ucieka_def(plansza, off, def_) if def_.id == self.id else self.ucieka_off(plansza, off, def_)
            elif kierunek == 3 and self._x > 0 and plansza[self._x - 1][self._y] is None:
                self._x -= 1
                return self.ucieka_def(plansza, off, def_) if def_.id == self.id else self.ucieka_off(plansza, off, def_)
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
                elif def_.zolwodparlatak:
                    return def_
            elif off.getSila() == def_.getSila():
                self.print_log(f"{off.getImie()} wygrywa z {def_.getImie()}")
                return off
            else:
                self.print_log(f"{off.getImie()} przegrywa z {def_.getImie()}")
                return def_
        return None
