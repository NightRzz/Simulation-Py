import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import simpledialog
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
import Base.Organizm as Organizm


class Swiat:
    def __init__(self, szerokosc, wysokosc):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.plansza = [[None for _ in range(szerokosc)] for _ in range(wysokosc)]
        self.gra = []
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
                for organism in self.gra:
                    if organism is not None and organism.get_x() == i and organism.get_y() == j and organism.get_sila() > -1 and organism.get_inicjatywa() > -1:
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
                self.gra.append(new_organism)
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
            new_organism.set_x(x)
            new_organism.set_y(y)

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

    def start(self):
        self.initialize_grid()
        self.root.mainloop()


# To start the application
if __name__ == "__main__":
    szerokosc = int(input("Podaj szerokosc mapy: "))
    wysokosc = int(input("Podaj wysokosc mapy: "))
    swiat = Swiat(szerokosc, wysokosc)
    swiat.start()
