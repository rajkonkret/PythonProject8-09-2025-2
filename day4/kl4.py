from abc import ABC, abstractmethod


# klasa abstrakcyjna
# nie można stworzyc obiektu tej klasy
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
class Ptak(ABC):
    def __init__(self, gatunek, szybkosc):
        """
        Klasa opsująca ptaka w pythonie
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # dekorator, metoda abstrakcyjna
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """
    Klasa Kura dziedziczy po klasie  Ptak
    """

    def __init__(self, gatunek):
        # obowiązkowo musimy wywołać konstruktor z klasy wyzszej
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_odglos(self):
        print("Ko ko k ok o")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


class Orzel(Ptak):
    """
    klasa dziedziczy po klasie Ptak
    """

    def wydaj_odglos(self):
        print("Kier kir kir kier")

    def polowanie(self):
        print('Tu', self.gatunek, "Rozpoczynam polowanie")


#
# or1 = Ptak("Orzeł", 45)
# or1.latam()  # Tu Orzeł Lecę z szybkością 45
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura domowa")
kur2.latam()  # Tu Kura domowa Ja nie latam.
kur2.wydaj_odglos()  # Ko ko k ok o

or2 = Orzel("Bielik", 55)
or2.latam()
or2.wydaj_odglos()
# Tu Bielik Lecę z szybkością 55
# Kier kir kir kier
lista = [kur2, or2]  # obiekty róznych klas
# polimorfizm
# obiekty róznych klas mogą być traktowane jako obiekty tej samej klasy w ramach wspolnych elementów
for i in lista:
    i.wydaj_odglos()
# Ko ko k ok o
# Kier kir kir kier
or2.polowanie()  # Tu Bielik Rozpoczynam polowanie
kur2.dziobanie()  # Tu Kura domowa Idę sobie podziobać
