import csv
import tkinter as tk
from tkinter import ttk, messagebox
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
        self.root.title("Yuriy Dyedyk 201316")
        self.grid = tk.Frame(self.root)
        self.grid.pack()
        self.log_area = tk.Text(self.root, width=50)
        self.log_area.pack()

    def print_log(self, message):
        # Use this method to print logs to the Text widget
        self.log_area.insert(tk.END, message + '\n')

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
            new_organism = Antylopa.Antylopa(self.print_log)
        elif idOrg == 'O':
            new_organism = Owca.Owca(self.print_log)
        elif idOrg == 'W':
            new_organism = Wilk.Wilk(self.print_log)
        elif idOrg == 'L':
            new_organism = Lis.Lis(self.print_log)
        elif idOrg == 'Z':
            new_organism = Zolw.Zolw(self.print_log)
        elif idOrg == 'T':
            new_organism = Trawa.Trawa(self.print_log)
        elif idOrg == 'M':
            new_organism = Mlecz.Mlecz(self.print_log)
        elif idOrg == 'J':
            new_organism = WilczeJagody.WilczeJagody(self.print_log)
        elif idOrg == 'G':
            new_organism = Guarana.Guarana(self.print_log)
        elif idOrg == 'B':
            new_organism = Barszcz.Barszcz(self.print_log)
        elif idOrg == 'C':
            new_organism = Czlowiek.Czlowiek(self.print_log)
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
        self.log_area.delete('1.0', tk.END)
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

            messagebox.showinfo("Zapis", "Zapisano stan gry do pliku!")
        except IOError as e:
            messagebox.showinfo("Zapis", "Error: {str(e)}")

    def wczytaj(self, file_path):
        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                line = next(reader)
                self.wysokosc = int(line[0])
                self.szerokosc = int(line[1])
                licznik = int(line[2])
                cooldown = int(line[3])
                wlacz = bool(line[4])
                self.Gra.clear()
                self.plansza = [[None for _ in range(self.szerokosc)] for _ in range(self.wysokosc)]
                for line in reader:
                    x = int(line[0])
                    y = int(line[1])
                    sila = int(line[2])
                    sign = line[3]
                    wiek = int(line[4])
                    if sign == 'A':
                        org = Antylopa.Antylopa(self.print_log, x, y, sila, wiek)
                    elif sign == 'B':
                        org = Barszcz.Barszcz(self.print_log, x, y, sila, wiek)
                    elif sign == 'C':
                        org = Czlowiek.Czlowiek(self.print_log, x, y, sila, wiek, cooldown, licznik, wlacz)
                    elif sign == 'G':
                        org = Guarana.Guarana(self.print_log, x, y, sila, wiek)
                    elif sign == 'L':
                        org = Lis.Lis(self.print_log, x, y, sila, wiek)
                    elif sign == 'M':
                        org = Mlecz.Mlecz(self.print_log, x, y, sila, wiek)
                    elif sign == 'O':
                        org = Owca.Owca(self.print_log, x, y, sila, wiek)
                    elif sign == 'T':
                        org = Trawa.Trawa(self.print_log, x, y, sila, wiek)
                    elif sign == 'J':
                        org = WilczeJagody.WilczeJagody(self.print_log, x, y, sila, wiek)
                    elif sign == 'W':
                        org = Wilk.Wilk(self.print_log, x, y, sila, wiek)
                    elif sign == 'Z':
                        org = Zolw.Zolw(self.print_log, x, y, sila, wiek)
                    else:
                        org = None
                    self.plansza[x][y] = org
                    self.Gra.append(org)
            messagebox.showinfo("Information", "Zapis gry zostal wczytany!")
            self.log_area.delete('1.0', tk.END)
            self.update_grid()
        except (IOError, ValueError) as e:
            messagebox.showerror("Error", "Error: " + str(e))

    def start(self):
        self.generuj()
        self.initialize_grid()
        wykonaj_ture_button = tk.Button(self.root, text="Wykonaj Ture", command=self.wykonajTure)
        wykonaj_ture_button.pack()
        self.root.bind('<Left>', lambda event: self.wykonajTure(37))
        self.root.bind('<Up>', lambda event: self.wykonajTure(38))
        self.root.bind('<Right>', lambda event: self.wykonajTure(39))
        self.root.bind('<Down>', lambda event: self.wykonajTure(40))
        self.root.bind('1', lambda event: self.wykonajTure(49))
        save_button = tk.Button(self.root, text="Zapisz", command=self.save_world_to_file)
        save_button.pack()
        load_button = tk.Button(self.root, text="Wczytaj", command=lambda: self.wczytaj('save.txt'))
        load_button.pack()
        self.root.mainloop()

    def rozsianie(self, kierunek, org):
        if kierunek == 0:
            if org.getY() > 0 and self.plansza[org.getX()][org.getY() - 1] is None:
                new_plant = self.dodaj_organizm(org.getX(), org.getY() - 1, org.getID())
                self.plansza[org.getX()][org.getY() - 1] = new_plant
                self.Gra.append(new_plant)
                self.print_log(f"{org.getImie()} rozsial sie na pole {org.getX()} {org.getY()}")
        elif kierunek == 1:
            if org.getY() < self.szerokosc - 1 and self.plansza[org.getX()][org.getY() + 1] is None:
                new_plant = self.dodaj_organizm(org.getX(), org.getY() + 1, org.getID())
                self.plansza[org.getX()][org.getY() + 1] = new_plant
                self.Gra.append(new_plant)
                self.print_log(f"{org.getImie()} rozsial sie na pole {org.getX()} {org.getY()}")
        elif kierunek == 2:
            if org.getX() < self.wysokosc - 1 and self.plansza[org.getX() + 1][org.getY()] is None:
                new_plant = self.dodaj_organizm(org.getX() + 1, org.getY(), org.getID())
                self.plansza[org.getX() + 1][org.getY()] = new_plant
                self.Gra.append(new_plant)
                self.print_log(f"{org.getImie()} rozsial sie na pole {org.getX()} {org.getY()}")
        elif kierunek == 3:
            if org.getX() > 0 and self.plansza[org.getX() - 1][org.getY()] is None:
                new_plant = self.dodaj_organizm(org.getX() - 1, org.getY(), org.getID())
                self.plansza[org.getX() - 1][org.getY()] = new_plant
                self.Gra.append(new_plant)
                self.print_log(f"{org.getImie()} rozsial sie na pole {org.getX()} {org.getY()}")

    def rozmnoz(self, org, rand, i, x1, y1):
        org.rozmnoz = False
        org.zolwodparlatak = False
        obronca = self.plansza[org.getX()][org.getY()]
        atakujacy = org.getID()

        # Check if the two organisms are of the same type
        if isinstance(org, type(obronca)):
            # Find a nearby empty location
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x1 + dx, y1 + dy
                if (0 <= new_x < self.wysokosc and 0 <= new_y < self.szerokosc and
                        self.plansza[new_x][new_y] is None):
                    # Create a new organism of the same type and place it in the empty location
                    new_organism = self.dodaj_organizm(new_x, new_y, org.getID())
                    self.plansza[new_x][new_y] = new_organism
                    self.Gra.append(new_organism)
                    self.print_log(f"{org.getImie()} rozmnozyl sie na pole {new_x} {new_y}")
                    return
            org.setX(x1)
            org.setY(y1)
            return

        # If the two organisms are not of the same type, proceed with the existing collision logic
        self.plansza[org.getX()][org.getY()] = org.kolizja(org, self.plansza[org.getX()][org.getY()], self.plansza,
                                                           self.szerokosc, self.wysokosc)
        if self.plansza[org.getX()][org.getY()] is not None and atakujacy == self.plansza[org.getX()][
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
