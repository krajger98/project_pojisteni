
from databaze_pojistencu import Databaze_pojistencu
import os


if __name__ == "__main__":

    vyber_akci = -1
    databaze_pojistencu = Databaze_pojistencu()

    while(vyber_akci != 4):

        os.system("cls")

        print("-----------------------")
        print("Evidence pojištěných")
        print("-----------------------")


        print("Vyberte si akci:")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")

        vyber_akci = int(input())

        match(vyber_akci):
            case 1:
                databaze_pojistencu.pridat_pojistence()
            case 2:
                databaze_pojistencu.vypsat_pojistence()
                input("\nPokračujte enterem")
            case 3:
                databaze_pojistencu.vyhledat_pojistence()
                input("\nPokračujte enterem")

            case _: pass



