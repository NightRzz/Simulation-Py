class Organizm:
    def __init__(self, x, y, id, imie, sila, inicjatywa):
        self.x = x
        self.y = y
        self.id = id
        self.imie = imie
        self.sila = sila
        self.inicjatywa = inicjatywa
        self.rozsiane = False
        self.rozmnoz = False
        self.cooldown = 0
        self.licznik = 0
        self.wlacz = False
        self.zolwodparlatak = False
        self.wiek = 0

    def set_cooldown(self, cooldown):
        self.cooldown = cooldown

    def set_licznik(self, licznik):
        self.licznik = licznik

    def set_wlacz(self, wlacz):
        self.wlacz = wlacz

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

    def get_id(self):
        return self.id

    def get_imie(self):
        return self.imie

    def set_imie(self, imie):
        self.imie = imie

    def get_sila(self):
        return self.sila

    def set_sila(self, sila):
        self.sila = sila

    def get_inicjatywa(self):
        return self.inicjatywa

    def set_inicjatywa(self, inicjatywa):
        self.inicjatywa = inicjatywa

    def get_wiek(self):
        return self.wiek

    def set_id(self, id):
        self.id = id

    def set_wiek(self, wiek):
        self.wiek = wiek

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        pass

    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        pass