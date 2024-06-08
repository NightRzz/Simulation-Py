import random
from Base.Zwierze import Zwierze



class Antylopa(Zwierze):
    def __init__(self,print_log, x=0, y=0, sila=4, wiek=0):
        super().__init__(x, y, 'A', "Antylopa", sila, 4)
        self.wiek = wiek
        self.print_log = print_log

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        kierunek = random.randint(0, 3)
        if kierunek == 0 and self.y > 1:
            self.y -= 2
        elif kierunek == 1 and self.y < szerokosc - 2:
            self.y += 2
        elif kierunek == 2 and self.x < wysokosc - 2:
            self.x += 2
        elif kierunek == 3 and self.x > 1:
            self.x -= 2

    def ucieka_def(self, plansza, off, def_):
        plansza[self.x][self.y] = def_
        self.print_log(f"{self.imie} ucieka przed {off.imie} na pole {self.x} {self.y}")
        return off

    def ucieka_off(self, plansza, off, def_):
        plansza[self.x][self.y] = off
        self.print_log(f"{self.imie} ucieka przed {def_.imie} na pole {self.x} {self.y}")
        return def_

    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        ucieczka = random.randint(0, 1)
        if def_.id == off.id:
            self.rozmnoz = True
            return off
        elif ucieczka == 1 and isinstance(def_, Zwierze):
            kierunek = random.randint(0, 3)
            if kierunek == 0 and self.y > 0 and plansza[self.x][self.y - 1] is None:
                self.y -= 1
                return self.ucieka_def(plansza, off, def_) if def_.id == self.id else self.ucieka_off(plansza, off, def_)
            elif kierunek == 1 and self.y < szerokosc - 1 and plansza[self.x][self.y + 1] is None:
                self.y += 1
                return self.ucieka_def(plansza, off, def_) if def_.id == self.id else self.ucieka_off(plansza, off, def_)
            elif kierunek == 2 and self.x < wysokosc - 1 and plansza[self.x + 1][self.y] is None:
                self.x += 1
                return self.ucieka_def(plansza, off, def_) if def_.id == self.id else self.ucieka_off(plansza, off, def_)
            elif kierunek == 3 and self.x > 0 and plansza[self.x - 1][self.y] is None:
                self.x -= 1
                return self.ucieka_def(plansza, off, def_) if def_.id == self.id else self.ucieka_off(plansza, off, def_)
        elif def_.id == self.id:  # broni
            if def_.sila > off.sila:
                self.print_log(f"{def_.imie} wygrywa z {off.imie}")
                return def_
            else:
                self.print_log(f"{def_.imie} przegrywa z {off.imie}")
                return off
        elif off.id == self.id:  # atakuje
            if off.sila > def_.sila:
                if off == def_.kolizja(off, def_, plansza, szerokosc, wysokosc):
                    self.print_log(f"{off.imie} wygrywa z {def_.imie}")
                    return off
                elif def_.zolwodparlatak:
                    return def_
            elif off.sila == def_.sila:
                self.print_log(f"{off.imie} wygrywa z {def_.imie}")
                return off
            else:
                self.print_log(f"{off.imie} przegrywa z {def_.imie}")
                return def_
        return None
