from kosar import Kosar

class Bolt:
    """
    A vásárlásokat kezelő osztály. Az osztály egyetlen attribútuma a kosarak listája.
    """

    def __init__(self, kosarak_listaja:str):
        """
        A bolt létrehozásakor beállítja az osztály attribútumait.
        """
        self.kosarak_listaja = kosarak_listaja

    def feladat_1(self, filepath: str) -> None:
        """
        Beolvassa a fájlból a kosarak tartalmát.

        :param filepath: A kosarak tartalmát tartalmazó fájl elérési útvonala.
        """
        try:
            lista = []
            f = open("kosar.txt", "r", encoding="UTF-8")

            for sor in f:
                sor = sor.strip().split()
                lista.append(sor)

            f.close()
            print("1. feladat: A kosar.txt beolvasva!")
        except FileExistsError:
            print("Hiba!")
        return lista

    lista = feladat_1()

    def feladat_2(self) -> None:
        """
        Kiírja, hányan fizettek a pénztárnál.
        """
        counter = [0]
        for sor in lista:
            if sor[0] == "F":
                counter[0] += sor[1]
        print("2. feladat: A pénztárnál fizettek: ", counter)

    def feladat_3(self) -> None:
        """
        Bekéri egy vásárlás sorszámát és kiírja:
            - hány darab árucikk volt a kosárban,
            - mely árucikkekből és milyen mennyiségben vásároltak,
            - a vásárlás összegét.
        """
        sorszam = int(input("Feladat 3: Adja meg egy vásárlás sorszmámat: "))
        for sor in lista:
            if sor[0] != sorszam:
                sorszam += sor[1]
        print("Árucikkek száma: ", kosar.arucikk_mennyisegenek_lekerdezese(), "\n")
        print("Árucikkek/mennyiságük: ", kosar.termekek_lekerdezese(), kosar.arucikk_mennyisegenek_lekerdezese(), "\n")
        print("A vásárlás összege: ", kosar.osszeg_lekerdezese(), "\n")

    def feladat_4(self) -> None:
        """
        Bekéri egy árucikk nevét és kiírja:
            - melyik vásárlásnál vettek először a termékből
            - melyik vásárlásnál vettek utoljára a termékből
            - összesen hány alkalommal vásároltak a termékből
        """
        anev = input("4. feladat: Árucikk neve: ")
        for sor in lista:
            if sor[0] != anev:
                anev += sor[1]
                print(anev)

    def feladat_5(self, filepath: str) -> None:
        """
        Elmenti a megadott fájlba a vásárlásonként fizetendő összeget.
        Beolvassa a fájlból a kosarak tartalmát.

        :param filepath: A kosarak tartalmát tartalmazó fájl elérési útvonala.
        """
        f = open("osszeg.txt","w",encoding="UTF-8")
        kosartart = []
        for sor in lista:
            if sor[0] not in kosartart:
                kosartart.append(sor[0])
        kosartart.sort()