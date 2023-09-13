
from pojistenec import Pojistenec

class Databaze_pojistencu:
    def __init__(self):
        self.pojistenci = []

    def pridat_pojistence(self):
        jmeno = input("Zadej křestní jméno: ")
        prijmeni = input("Zadej příjmení: ")
        vek = input("Zadej věk: ")
        telefoni_cislo = input("Zadej telefoni cislo: ")

        pojistenec = Pojistenec(jmeno,prijmeni,vek,telefoni_cislo)
        self.pojistenci.append(pojistenec)

    def vypsat_pojistence(self):
        for pojistenec in self.pojistenci:
            print(f"{pojistenec.jmeno} {pojistenec.prijmeni}\t{pojistenec.vek}\t{pojistenec.telefoni_cislo}")

    def vyhledat_pojistence(self):
        jmeno = input("Zadejte jméno pojištěného: ")
        prijmeni = input("Zadejte příjmení pojištěného: ")

        for pojistenec in self.pojistenci:
            if(pojistenec.jmeno == jmeno and pojistenec.prijmeni == prijmeni):
                print(f"{pojistenec.jmeno} {pojistenec.prijmeni}\t{pojistenec.vek}\t{pojistenec.telefoni_cislo}")
