import random
from Base.Zwierze import Zwierze


class Owca(Zwierze):
    def __init__(self,print_log, x=0, y=0, sila=4, wiek=0):
        super().__init__(x, y, 'O', "Owca", sila, 4)
        self.wiek = wiek
        self.print_log = print_log

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        kierunek = random.randint(0, 3)
        if kierunek == 0 and self.y > 0:
            self.y -= 1
        elif kierunek == 1 and self.y < szerokosc - 1:
            self.y += 1
        elif kierunek == 2 and self.x < wysokosc - 1:
            self.x += 1
        elif kierunek == 3 and self.x > 0:
            self.x -= 1

    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        if def_.id == off.id:
            def_.rozmnoz = True
            return def_
        elif def_.id == self.id:  # broni
            if def_.sila > off.sila:
                self.print_log(f"{def_.imie} wygrywa z {off.imie}")
                return def_
            elif def_.sila == off.sila:
                self.print_log(f"{off.imie} wygrywa z {def_.imie}")
                return off
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
        return def_
