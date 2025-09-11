class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        """
        Konstruktor - metoda inicjalizująca
        :param model:
        :param year:
        """
        self.model = model
        self.year = year
        # hermetyzacja
        # enkapsulacja - hermetyzacja i stworzenie metod do odczytu i zapisu wartości pól
        # pole prywatne
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkośc wynosi: {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def __zmien_bieg(self):
        print("Zmiana biegu")


sam = Car("Opel", 2025)
sam.gaz()
sam.gaz()
sam.gaz()
sam.gaz()
sam.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(sam.__predkosc)  # 50
sam.licznik()  # Prędkośc wynosi: 50 km/h
sam.__predkosc = 0
sam.licznik()  # Prędkośc wynosi: 50 km/h
sam.hamuj()
sam.hamuj()
sam.hamuj()
sam.hamuj()
sam.hamuj()
sam.licznik()  # Prędkośc wynosi: 0 km/h
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Prędkośc wynosi: 0 km/h
