from Base.Zwierze import Zwierze


class Czlowiek(Zwierze):
    def __init__(self, print_log, x=0, y=0, sila=5, wiek=0, cooldown=6, licznik=0, wlacz=False):
        super().__init__(x, y, 'C', "Czlowiek", sila, 4)
        self.wiek = wiek
        self.cooldown = cooldown
        self.licznik = licznik
        self.wlacz = wlacz
        self.print_log = print_log

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        key = 0
        if keycode is not None:
            key = keycode
        if self.licznik == 0 and not self.wlacz:
            self.cooldown += 1
        if self.wlacz and self.cooldown > 5:
            if self.licznik < 6:
                self._sila -= 1
            else:
                self.wlacz = False
                self.licznik = 0
                self.cooldown = 0
                self.print_log("Umiejetnosc czlowieka przestala dzialac")
        else:
            self.cooldown += 1

        if key == 38 and self._x > 0:
            self._x -= 1
        elif key == 40 and self._x < wysokosc - 1:
            self._x += 1
        elif key == 37 and self._y > 0:
            self._y -= 1
        elif key == 39 and self._y < szerokosc - 1:
            self._y += 1
        elif key == 49:
            if self.cooldown < 10:
                self.print_log("Umiejetnosc czlowieka nie gotowa")
            elif not self.wlacz and self.cooldown > 10:
                self.print_log("Umiejetnosc czlowieka wlaczona")
                self._sila += 5
                self.wlacz = True

        self.print_log(f"Ruszasz sie na pole {self._x} {self._y} z sila {self._sila}")

    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        if def_.id == self.id:  # broni
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
                elif def_.zolwodparlatak:
                    return def_
            elif off.getSila() == def_.getSila():
                self.print_log(f"{off.getImie()} wygrywa z {def_.getImie()}")
                return off
            else:
                self.print_log(f"{off.getImie()} przegrywa z {def_.getImie()}")
                return def_
        return None
