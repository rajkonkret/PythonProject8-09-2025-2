# zbiór (set)  - przechowuje unikalne wartości (brak duplikatów)
# zbiór nie zachowuje kolejnosci przy dowaniu elemntów
# nie posiada indeksy

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(type(zbior)) # <class 'set'>
print(zbior) # {33, 66, 777, 11, 44, 22, 55}
