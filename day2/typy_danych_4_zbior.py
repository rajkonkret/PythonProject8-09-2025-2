# zbiór (set)  - przechowuje unikalne wartości (brak duplikatów)
# zbiór nie zachowuje kolejnosci przy dowaniu elemntów
# nie posiada indeksy
from day2.typy_danych_2_lista import krotka

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(type(zbior))  # <class 'set'>
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

# pusty zbiór
zb2 = set()
print(zb2)  # set()
print(type(zbior))  # <class 'set'>

# dodanie elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(33)
zbior.add(24)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 24}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24}

# pop() - usunie pierwszy element
print(zbior.pop())  # 33, usunie pierwszy element
print(zbior)  # {66, 777, 11, 44, 18, 22, 24}
zmienna = zbior.pop()
print("Zmienna:", zmienna)  # Zmienna: 66

zbior_copy = zbior.copy()  # kopia elemntów zbioru
print(zbior)
print(zbior_copy)
print(id(zbior))
print(id(zbior_copy))
# 2172198372512
# 2172198673696

zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}
print(zbior_2)  # {18, 667, 52, 11, 44, 12.34, 62}

# suma zbiorów - tworzy nowy zbiór
print(zbior | zbior_2)  # {777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}
print(zbior.union(zbior_2))  # {777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}

# częśc wspolna - tworzy nowy zbiór
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# róznica zbiorów
print(zbior - zbior_2)  # {24, 777, 22}
print(zbior.difference(zbior_2))  # {24, 777, 22}
print(zbior_2.difference(zbior))  # {667, 52, 12.34, 62}

# łączy zbiory, zmienia bazowy!!!
zbior.update(zbior_2)
print(zbior)  # {777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}

krotka = tuple(zbior)
print(krotka)  # (777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62)

lista = list(zbior)
print(lista)  # [777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62]

# sprawdzenie czy element znajduję sie w danej kolekcji
print(667 in zbior)  # True
print(777 in lista)  # True
print(777 in krotka)  # True
