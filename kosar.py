class Kosar:
    """
    Egyetlen vásárlás adatait kezelő osztály.

    Az osztály attribútumai:
        - a kosárban lévő árucikkek (név-mennyiség párok)
        - a vásárlás összege
    """
    def __init__(self, termekek: dict[str, int]) -> None:
        """
        A kosár létrehozásakor beállítja az osztály attribútumait.
        """
        self.osszeg_lekerdezese(int)
        self.termekek_lekerdezese(dict)
        self.termekek_szamanak_lekerdezese(int)
        self.arucikk_mennyisegenek_lekerdezese(int)
        self.kosar_tartalmanak_kiiratasa()

    def osszeg_lekerdezese(self, osszeg) -> int:
        """
        A vásárlás összegének lekérdezése.

        :return: A vásárlás összege Ft-ban.
        """
        vasarlas_osszege == 0
        for sor in lista:
            if sor[0] != "F":
                vasarlas_osszege += sor[1]

    def termekek_lekerdezese(self) -> dict[str, int]:
        """
        Az árucikk-mennyiség párok lekérdezése.

        :return: Az árucikkek nevei és mennyiségei.
        """

        return nev, menny

    def termekek_szamanak_lekerdezese(self) -> int:
        """
        A kosárban lévő termékek számának lekérdezése.

        :return: Hány darab termék van a kosárban.
        """
        for sor in lista:
            if sor[0] != "F":
                termek_szama += sor[1]
        return termekek_szama

    def arucikk_mennyisegenek_lekerdezese(self, arucikk: str) -> int:
        """
        Egy árucikknek a kosárban megtalálható mennyiségének lekérdezése.

        :param arucikk: A vizsgált árucikk neve.
        :return: A vizsgált árucikk mennyisége a kosárban.
        """
        arumenny == 0
        for sor in lista:
            if sor[0] != "F":
                arumenny += sor[1]
        return arumenny

    def kosar_tartalmanak_kiiratasa(self) -> None:
        """
        Kiírja a kosár tartalmát a konzolra.
        """

        print("A kosár tartalma: ",)
