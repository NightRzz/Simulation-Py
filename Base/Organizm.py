class Organizm:
    def __init__(self, x, y, orgid, imie, sila, inicjatywa):
        self.x = x
        self.y = y
        self.id = orgid
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

    def setCooldown(self, cooldown):
        self.cooldown = cooldown

    def setLicznik(self, licznik):
        self.licznik = licznik

    def setWlacz(self, wlacz):
        self.wlacz = wlacz

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def getID(self):
        return self.id

    def getImie(self):
        return self.imie

    def setImie(self, imie):
        self.imie = imie

    def getSila(self):
        return self.sila

    def setSila(self, sila):
        self.sila = sila

    def getInicjatywa(self):
        return self.inicjatywa

    def setInicjatywa(self, inicjatywa):
        self.inicjatywa = inicjatywa

    def getWiek(self):
        return self.wiek

    def setId(self, id):
        self.id = id

    def setWiek(self, wiek):
        self.wiek = wiek

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        pass

    def kolizja(self, off, def_, plansza, szerokosc, wysokosc):
        pass
