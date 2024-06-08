import random
from Base.Zwierze import Zwierze


class Zolw(Zwierze):
    def __init__(self,print_log, x=0, y=0, sila=2, wiek=0):
        super().__init__(x, y, 'Z', "Zolw", sila, 1)
        self.wiek = wiek
        self.zolwodparlatak = False
        self.print_log = print_log

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        ruch = random.randint(0, 2)
        if ruch == 0:
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
            if off.sila < 5:  # odparcie ataku
                self.print_log(f"{def_.imie} odpiera atak {off.imie}")
                self.zolwodparlatak = True
                return def_
            else:
                if def_.sila > off.sila:
                    self.print_log(f"{def_.imie} wygyrwa z {off.imie}")
                    return def_
                else:
                    self.print_log(f"{def_.imie} przegrywa z {off.imie}")
                    return off
        elif off.id == self.id:  # atakuje
            if off.sila > def_.sila:
                if off == def_.kolizja(off, def_, plansza, szerokosc, wysokosc):
                    self.print_log(f"{off.imie} wygyrwa z {def_.imie}")
                    return off
            elif off.sila == def_.sila:
                self.print_log(f"{off.imie} wygrywa z {def_.imie}")
                return off
            else:
                self.print_log(f"{off.imie} przegrywa z {def_.imie}")
                return def_
        return None
