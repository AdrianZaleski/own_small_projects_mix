import random
from time import sleep


# Definiowanie klasy wojownika o określonych atrybutach:
class Wojownik:
    def __init__(self, imie = "anonim", zycie = 0, pAtaku = 0, pObrony = 0):
        self.imie = imie
        self. zycie = zycie
        self.pAtaku = pAtaku
        self.pObrony = pObrony


    # Definicja funkcji atakowania - zakres obrażeń od 0 do punktów ataku:
    def atak(self):
        return random.randint(0, self.pAtaku) * random.randint(2, 5)    # Dodatkowe wzmocnienie siły ataku


    # Definicja funkcji obrony - zakres obrony od 0 do punktów obrony:
    def obrona(self):
        return random.randint(0, self.pObrony)


    # Definicja funkcji straconego życia w walce:
    def stracone_zycie(self, ilosc):
        self.zycie -= ilosc
        if self.zycie <= 0:
            print(f'{self.imie} poległ w walce')


    # Funkca czy żywy:
    def czy_zywy(self):
        if self.zycie <= 0:
            return False
        else:
            return True


    # Definicja wyswietlania imienia
    def __str__(self):
        return self.imie


# Funkcja odpowiedzialna za walkę:
def walka (malpa, rycerz):
    i = 1
    # Sprawdzenie warunku czy któryś z przeciwników jest żywy:
    while (malpa.czy_zywy() and rycerz.czy_zywy()):
        print(f"Runda numer: {i}")
        wyswietl_staty(malpa, rycerz)

        # Losowanie kto ma atakować:
        if random.randint(0, 1) == 0:
            pojedynek(malpa, rycerz)
        else:
            pojedynek(rycerz, malpa)

        # Sprawdzenie kto jeszcze żyje:
        if rycerz.czy_zywy() == True and malpa.czy_zywy() == True:
           print("\nObaj przeciwnycy walczą nadal\n")
        elif rycerz.czy_zywy() == True and malpa.czy_zywy() == False:
            print(f"\n{rycerz.imie} wygrał walkę\n")
        else:
             print(f"\n{malpa.imie} wygrał walkę\n")

        # Chwila odstępu - sleep jest w sekundach!
        print(" ")
        sleep(2)
        i += 1  # Wzrost kolejnej walki


def pojedynek (x, y):
    print(f"{x} został zaatakowany przez {y}")
    if y.atak() > x.obrona():
        obrazenia = y.atak() - x.obrona()
        print(f"{x} stracił {obrazenia} punktów życia")
        x.stracone_zycie(obrazenia)
    else:
        print(f"Atak {y} jest za słaby by pokonać obronę {x}")


def wyswietl_staty(x, y):
    for i in (x, y):
        print(f"{i} ma {i.zycie} punktów życia")


# Wywołanie klasy Wojownik w celu utworzenia wojownika o określonych parametrach:
rycerz = Wojownik("Rycerz", random.randint(10, 100), random.randint(10, 50), random.randint(5, 30))
malpa = Wojownik("Małpi Wojownik", random.randint(10, 100), random.randint(10, 50), random.randint(5, 30))

# Uruchomienie funkcji walki między przeciwnikami:
walka(malpa, rycerz)