import tkinter as tk
from tkinter import ttk
import random
import Zwierzeta.Antylopa as Antylopa
import Zwierzeta.Owca as Owca
import Zwierzeta.Wilk as Wilk
import Zwierzeta.Lis as Lis
import Zwierzeta.Zolw as Zolw
import Rosliny.Trawa as Trawa
import Rosliny.Mlecz as Mlecz
import Rosliny.WilczeJagody as WilczeJagody
import Rosliny.Guarana as Guarana
import Rosliny.Barszcz as Barszcz
import Zwierzeta.Czlowiek as Czlowiek
from Base.Roslina import Roslina
from Base.Zwierze import Zwierze


class Swiat:
    def __init__(self, szerokosc, wysokosc):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.plansza = [[None for _ in range(szerokosc)] for _ in range(wysokosc)]
        self.Gra = []
        self.color_map = {
            'A': '#A88319',  # Antylopa
            'O': '#EDC3C7',  # Owca
            'W': '#75736E',  # Wilk
            'L': '#D98A02',  # Lis
            'Z': '#BDA573',  # Zolw
            'T': '#07F20B',  # Trawa
            'M': '#E1E81A',  # Mlecz
            'J': '#0B083D',  # WilczeJagody
            'G': '#DB6556',  # Guarana
            'B': '#B0DEA2',  # Barszcz
            'C': '#F2E5CB'  # Czlowiek
        }
        self.root = tk.Tk()
        self.root.title("Yuriy Dyedyk")
        self.grid = tk.Frame(self.root)
        self.grid.pack()

    def initialize_grid(self):
        for widget in self.grid.winfo_children():
            widget.destroy()

        for i in range(self.wysokosc):
            for j in range(self.szerokosc):
                square = tk.Button(self.grid, height=2, width=4)
                square.grid(row=i, column=j)
                organism_found = False
                for organism in self.Gra:
                    if (organism is not None and organism.getX() == i and organism.getY() == j
                            and organism.getSila() > -1 and organism.getInicjatywa() > -1):
                        organism_found = True
                        square.config(text=organism.id, bg=self.color_map[organism.id])
                        break
                if not organism_found:
                    square.config(command=lambda x=i, y=j: self.add_organism(x, y))

    def add_organism(self, x, y):
        options = ["Antylopa", "Owca", "Wilk", "Lis", "Zolw", "Trawa", "Mlecz", "JagodyWilcze", "Guarana", "Barszcz",
                   "Czlowiek"]

        def ok():
            inputOrg = combo.get()
            if inputOrg in options:
                idOrg = inputOrg[0]
                new_organism = self.dodaj_organizm(x, y, idOrg)
                self.plansza[x][y] = new_organism
                self.Gra.append(new_organism)
                self.update_grid()
            top.destroy()

        top = tk.Toplevel(self.root)
        top.title("Organism Choice")
        label = tk.Label(top, text="Choose organism")
        label.pack()
        combo = ttk.Combobox(top, values=options)
        combo.pack()
        button = tk.Button(top, text="OK", command=ok)
        button.pack()

    def update_grid(self):
        self.initialize_grid()

    def dodaj_organizm(self, x, y, idOrg):
        new_organism = None
        if idOrg == 'A':
            new_organism = Antylopa.Antylopa()
        elif idOrg == 'O':
            new_organism = Owca.Owca()
        elif idOrg == 'W':
            new_organism = Wilk.Wilk()
        elif idOrg == 'L':
            new_organism = Lis.Lis()
        elif idOrg == 'Z':
            new_organism = Zolw.Zolw()
        elif idOrg == 'T':
            new_organism = Trawa.Trawa()
        elif idOrg == 'M':
            new_organism = Mlecz.Mlecz()
        elif idOrg == 'J':
            new_organism = WilczeJagody.WilczeJagody()
        elif idOrg == 'G':
            new_organism = Guarana.Guarana()
        elif idOrg == 'B':
            new_organism = Barszcz.Barszcz()
        elif idOrg == 'C':
            new_organism = Czlowiek.Czlowiek()
        if new_organism is not None:
            new_organism.setX(x)
            new_organism.setY(y)

        return new_organism

    def generuj(self):
        i = 0
        while i < 15:
            randy = random.randint(0, self.szerokosc - 1)
            randx = random.randint(0, self.wysokosc - 1)
            if self.plansza[randx][randy] is None:
                if i < 2:
                    self.plansza[randx][randy] = self.dodaj_organizm(randx, randy, 'W')
                elif i < 3:
                    self.plansza[randx][randy] = self.dodaj_organizm(randx, randy, 'C')
                elif i < 4:
                    self.plansza[randx][randy] = self.dodaj_organizm(randx, randy, 'A')
                elif i < 5:
                    self.plansza[randx][randy] = self.dodaj_organizm(randx, randy, 'L')
                elif i < 7:
                    self.plansza[randx][randy] = self.dodaj_organizm(randx, randy, 'Z')
                elif i < 8:
                    self.plansza[randx][randy] = self.dodaj_organizm(randx, randy, 'T')
                elif i < 10:
                    self.plansza[randx][randy] = self.dodaj_organizm(randx, randy, 'M')
                elif i < 11:
                    self.plansza[randx][randy] = self.dodaj_organizm(randx, randy, 'J')
                elif i < 12:
                    self.plansza[randx][randy] = self.dodaj_organizm(randx, randy, 'B')
                elif i < 13:
                    self.plansza[randx][randy] = self.dodaj_organizm(randx, randy, 'O')
                else:
                    self.plansza[randx][randy] = self.dodaj_organizm(randx, randy, 'G')
                i += 1
        self.Gra = [organism for row in self.plansza for organism in row if organism is not None]

    def wykonajTure(self, keycode=None):
        self.zakonczTure()

        rand = random.Random()
        for i in range(len(self.Gra) - 1, -1, -1):
            org = self.Gra[i]
            if org is not None:
                x1 = org.getX()
                y1 = org.getY()
                org.rozsiane = False
                org.akcja(self.plansza, self.Gra, self.szerokosc, self.wysokosc, keycode)
                if org.getID() == 'C' and org.wlacz:
                    org.licznik += 1
                if isinstance(org, Roslina) and org.rozsiane:
                    kierunek = rand.randint(0, 3)
                    self.rozsianie(kierunek, org)
                elif self.plansza[org.getX()][org.getY()] == self.plansza[x1][y1]:
                    self.plansza[org.getX()][org.getY()] = org
                elif self.plansza[org.getX()][org.getY()] is None:
                    self.plansza[org.getX()][org.getY()] = org
                    self.plansza[x1][y1] = None
                elif isinstance(org, Zwierze) and self.plansza[org.getX()][org.getY()] is not None:
                    self.rozmnoz(org, rand, i, x1, y1)
        self.update_grid()

    def zakonczTure(self):
        if len(self.Gra) > 0:
            self.Gra[0] = None
        self.Gra.clear()
        for i in range(self.wysokosc):
            for j in range(self.szerokosc):
                if self.plansza[i][j] is not None:
                    self.Gra.append(self.plansza[i][j])
        if len(self.Gra) > 0:
            self.Gra.sort(key=lambda org: (-org.getInicjatywa(), -org.getWiek()))
        for org in self.Gra:
            if org is not None:
                org.setWiek(org.getWiek() + 1)

    def save_world_to_file(self):
        try:
            with open('save.txt', 'w') as file:
                licznik = 0
                cooldown = 0
                wlacz = False
                for org in self.Gra:
                    if org is not None and org.getID() == 'C':
                        licznik = org.licznik
                        cooldown = org.cooldown
                        wlacz = org.wlacz
                        break
                file.write(f"{self.wysokosc},{self.szerokosc},{licznik},{cooldown},{wlacz}\n")

                for org in self.Gra:
                    if org is not None:
                        file.write(f"{org.getX()},{org.getY()},{org.getSila()},{org.getID()},{org.getWiek()}\n")

            print("Zapisano stan gry do pliku!")
        except IOError as e:
            print(f"Error: {str(e)}")

    def start(self):
        self.generuj()
        self.initialize_grid()
        wykonaj_ture_button = tk.Button(self.root, text="Wykonaj Ture", command=self.wykonajTure)
        wykonaj_ture_button.pack()
        self.root.bind('<Left>', lambda event: self.wykonajTure(37))  # ASCII value for left arrow key is 37
        self.root.bind('<Up>', lambda event: self.wykonajTure(38))  # ASCII value for up arrow key is 38
        self.root.bind('<Right>', lambda event: self.wykonajTure(39))  # ASCII value for right arrow key is 39
        self.root.bind('<Down>', lambda event: self.wykonajTure(40))  # ASCII value for down arrow key is 40

        self.root.mainloop()

    def rozsianie(self, kierunek, org):
        if kierunek == 0:
            if org.getY() > 0 and self.plansza[org.getX()][org.getY() - 1] is None:
                new_plant = self.dodaj_organizm(org.getX(), org.getY() - 1, org.getID())
                self.plansza[org.getX()][org.getY() - 1] = new_plant
                self.Gra.append(new_plant)
                print(f"{org.getImie()} rozsial sie na pole {org.getX()} {org.getY()}")
        elif kierunek == 1:
            if org.getY() < self.szerokosc - 1 and self.plansza[org.getX()][org.getY() + 1] is None:
                new_plant = self.dodaj_organizm(org.getX(), org.getY() + 1, org.getID())
                self.plansza[org.getX()][org.getY() + 1] = new_plant
                self.Gra.append(new_plant)
                print(f"{org.getImie()} rozsial sie na pole {org.getX()} {org.getY()}")
        elif kierunek == 2:
            if org.getX() < self.wysokosc - 1 and self.plansza[org.getX() + 1][org.getY()] is None:
                new_plant = self.dodaj_organizm(org.getX() + 1, org.getY(), org.getID())
                self.plansza[org.getX() + 1][org.getY()] = new_plant
                self.Gra.append(new_plant)
                print(f"{org.getImie()} rozsial sie na pole {org.getX()} {org.getY()}")
        elif kierunek == 3:
            if org.getX() > 0 and self.plansza[org.getX() - 1][org.getY()] is None:
                new_plant = self.dodaj_organizm(org.getX() - 1, org.getY(), org.getID())
                self.plansza[org.getX() - 1][org.getY()] = new_plant
                self.Gra.append(new_plant)
                print(f"{org.getImie()} rozsial sie na pole {org.getX()} {org.getY()}")

    def rozmnoz(self, org, rand, i, x1, y1):
        org.rozmnoz = False
        org.zolwodparlatak = False
        obronca = self.plansza[org.getX()][org.getY()]
        atakujacy = org.getID()
        self.plansza[org.getX()][org.getY()] = org.kolizja(org, self.plansza[org.getX()][org.getY()], self.plansza,
                                                           self.szerokosc, self.wysokosc)
        if org.rozmnoz:
            kierunek = rand.randint(0, 3)
            new_x, new_y = x1, y1
            if kierunek == 0 and org.getY() > 0:  # move up
                new_y -= 1
            elif kierunek == 1 and org.getY() < self.szerokosc - 1:  # move down
                new_y += 1
            elif kierunek == 2 and org.getX() > 0:  # move left
                new_x -= 1
            elif kierunek == 3 and org.getX() < self.wysokosc - 1:  # move right
                new_x += 1

            if self.plansza[new_x][new_y] is None:
                new_organism = self.dodaj_organizm(new_x, new_y, org.getID())
                self.plansza[new_x][new_y] = new_organism
                self.Gra.append(new_organism)
                print(f"{org.getImie()} rozmnozyl sie na pole {new_x} {new_y}")
        elif self.plansza[org.getX()][org.getY()] is not None and atakujacy == self.plansza[org.getX()][
            org.getY()].getID():
            for j in range(len(self.Gra)):
                if self.Gra[j] is not None and obronca == self.Gra[j]:
                    self.Gra[j] = None
            self.plansza[x1][y1] = None
        else:
            if obronca.getID() != 'Z' and not obronca.zolwodparlatak:
                self.Gra[i] = None
                self.plansza[x1][y1] = None
            else:
                org.setX(x1)
                org.setY(y1)


# To start the application
if __name__ == "__main__":
    szerokosc = int(input("Podaj szerokosc mapy: "))
    wysokosc = int(input("Podaj wysokosc mapy: "))
    swiat = Swiat(szerokosc, wysokosc)
    swiat.start()
