import random
from Base.Zwierze import Zwierze


class CyberOwca(Zwierze):
    def __init__(self, print_log, x=0, y=0, sila=11, wiek=0):
        super().__init__(x, y, 'K', "CyberOwca", sila, 4)
        self.wiek = wiek
        self.print_log = print_log

    def znajdz_najblizszy_barszcz(self, plansza, szerokosc, wysokosc):
        barszcz = None
        blizszaOdleglosc = float('inf')
        for x in range(szerokosc):
            for y in range(wysokosc):
                org = plansza[x][y]
                if org and org.getImie() == "Barszcz Sosnowskiego":
                    odleglosc = abs(self._x - x) + abs(self._y - y)
                    if odleglosc < blizszaOdleglosc:
                        blizszaOdleglosc = odleglosc
                        barszcz = org

        return barszcz

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        barszcz = self.znajdz_najblizszy_barszcz(plansza, szerokosc, wysokosc)
        if barszcz:
            if barszcz.getX() < self._x:
                self._x -= 1
            elif barszcz.getX() > self._x:
                self._x += 1
            elif barszcz.getY() < self._y:
                self._y -= 1
            elif barszcz.getY() > self._y:
                self._y += 1
        else:
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
        if def_.getImie() == "Barszcz Sosnowskiego":
            self.print_log(f"{off.getImie()} zjada {def_.getImie()}")
            return off
        elif def_.id == off.id:
            def_.rozmnoz = True
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
