# klasa  - element programowania obiektowego
# klasa - przepis, szablon
# cechy (zmienne)
# metody  - funkcje w klasie
# obiekt - instancja klasy
# klasa musi zostac zadekalrowana przed użyciem
# # tworzenie obiektu klasy uruchumia funkcję inicjalizującą (konstruktor) __init__
# paradygmaty -> hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

# PascalCase, UpperCamelCase
class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam się: {self.imie}")
        # print(f"Nazywam się: {cz1.imie}")


print(Human.__doc__)
# dokumentacja klasy
# Klasa Human opisująca człowieka w pythonie
# cd day4 - przejście do katalogu day4
# pydoc -b - serwer dokumentacyjny
# pydoc -w kl1

# tworzenie obiektu klasy
cz1 = Human()
print(cz1)
# <__main__.Human object at 0x000002650FE96F90>
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
#
# None
# k

cz1.imie = "Anna"
cz1.wiek = 34
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Anna
# 34
# k

cz2 = Human()
cz2.imie = 'Radek'
cz2.wiek = 67
cz2.plec = "m"
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
# Radek
# 67
# m

cz1.powitanie()
# Nazywam się: Anna
cz2.powitanie()  # Nazywam się: Radek
