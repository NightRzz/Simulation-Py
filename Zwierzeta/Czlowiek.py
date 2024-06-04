from Base.Zwierze import Zwierze


class Czlowiek(Zwierze):
    def __init__(self, x=0, y=0, sila=5, wiek=0, cooldown=6, licznik=0, wlacz=False):
        super().__init__(x, y, 'C', "Czlowiek", sila, 4)
        self.wiek = wiek
        self.cooldown = cooldown
        self.licznik = licznik
        self.wlacz = wlacz

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        key = 0
        if keycode is not None:
            key = keycode
            keycode = 0
        if self.licznik == 0 and not self.wlacz:
            self.cooldown += 1
        if self.wlacz and self.cooldown > 5:
            if self.licznik < 6:
                self.sila -= 1
            else:
                self.wlacz = False
                self.licznik = 0
                self.cooldown = 0
                print("Umiejetnosc czlowieka przestala dzialac")
        else:
            self.cooldown += 1

        if key == 38 and self.x > 0:
            self.x -= 1
        elif key == 40 and self.x < wysokosc - 1:
            self.x += 1
        elif key == 37 and self.y > 0:
            self.y -= 1
        elif key == 39 and self.y < szerokosc - 1:
            self.y += 1
        elif key == 49:
            if self.cooldown < 10:
                print("Umiejetnosc czlowieka nie gotowa")
            elif not self.wlacz and self.cooldown > 10:
                print("Umiejetnosc czlowieka wlaczona")
                self.sila += 5
                self.wlacz = True

        print(f"Ruszasz sie na pole {self.x} {self.y} z sila {self.sila}")

    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        if def_.id == self.id:  # broni
            if def_.sila > off.sila:
                print(f"{def_.imie} wygyrwa z {off.imie}")
                return def_
            else:
                print(f"{def_.imie} przegrywa z {off.imie}")
                return off
        elif off.id == self.id:  # atakuje
            if off.sila > def_.sila:
                if off == def_.kolizja(off, def_, plansza, szerokosc, wysokosc):
                    print(f"{off.imie} wygyrwa z {def_.imie}")
                    return off
                elif def_.zolwodparlatak:
                    return def_
            elif off.sila == def_.sila:
                print(f"{off.imie} wygrywa z {def_.imie}")
                return off
            else:
                print(f"{off.imie} przegrywa z {def_.imie}")
                return def_
        return None
