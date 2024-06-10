class Organizm:
    def __init__(self, x, y, orgid, imie, sila, inicjatywa):
        self.id = orgid
        self.rozsiane = False
        self.rozmnoz = False
        self.cooldown = 0
        self.licznik = 0
        self.wlacz = False
        self.zolwodparlatak = False

        self._x = x
        self._y = y
        self._imie = imie
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._wiek = 0

    def setCooldown(self, cooldown):
        self.cooldown = cooldown

    def setLicznik(self, licznik):
        self.licznik = licznik

    def setWlacz(self, wlacz):
        self.wlacz = wlacz

    def setX(self, x):
        self._x = x

    def getX(self):
        return self._x

    def setY(self, y):
        self._y = y

    def getY(self):
        return self._y

    def getID(self):
        return self.id

    def getImie(self):
        return self._imie

    def setImie(self, imie):
        self._imie = imie

    def getSila(self):
        return self._sila

    def setSila(self, sila):
        self._sila = sila

    def getInicjatywa(self):
        return self._inicjatywa

    def setInicjatywa(self, inicjatywa):
        self._inicjatywa = inicjatywa

    def getWiek(self):
        return self._wiek

    def setId(self, id):
        self.id = id

    def setWiek(self, wiek):
        self._wiek = wiek

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        pass

    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        pass
