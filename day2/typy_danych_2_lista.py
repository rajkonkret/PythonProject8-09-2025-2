# kolekcje
from sys import base_prefix

# lista - przechowuje dowolną ilosc danych, różnego typu na raz
# zachowuje kolejnosć przy doawania elementów

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(type(pusta_lista))  # <class 'list'>
print(pusta_lista)  # []

# append() - dodanie elementów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Ola")
lista.append("Aga")
lista.append("Kamil")
lista.append("Adam")
lista.append("Bogdan")

print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Ola', 'Aga', 'Kamil', 'Adam', 'Bogdan']
#     0         1       2       3      4       5        6        7

print(len(lista))  # 8 elementów

print(lista[2])  # Zenek
print(lista[4])  # element numer 5,Aga

# print(lista[10])  # IndexError: list index out of range

# ['Radek', 'Tomek', 'Zenek', 'Ola', 'Aga', 'Kamil', 'Adam', 'Bogdan']
#     0         1       2       3      4       5        6        7
#     -8        -7      -6      -5     -4      -3      -2        -1
print(lista[7])  # Bogdan, ostatni element
print(lista[len(lista) - 1])  # Bogdan
print(lista[-1])  # ostatni element
print(lista[-3])  # Kamil

# slicowanie - wyswietlanie fragmentów listy
print(lista[0:3])  # ['Radek', 'Tomek', 'Zenek'] indeksy 012
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']

print(lista[2:])  # z ostatnim włącznie
# ['Zenek', 'Ola', 'Aga', 'Kamil', 'Adam', 'Bogdan']
print(lista[2:7])  # bez ostatniego
# ['Zenek', 'Ola', 'Aga', 'Kamil', 'Adam']

print(lista[2:20])  # ['Zenek', 'Ola', 'Aga', 'Kamil', 'Adam', 'Bogdan']
print(lista[12:56])  # []
print(lista[2:2])  # []
print(lista[2:3])  # ['Zenek']

print(lista[:])
# ['Radek', 'Tomek', 'Zenek', 'Ola', 'Aga', 'Kamil', 'Adam', 'Bogdan']

# ['Radek', 'Tomek', 'Zenek', 'Ola', 'Aga', 'Kamil', 'Adam', 'Bogdan']
#     0         1       2       3      4       5        6        7
#     -8        -7      -6      -5     -4      -3      -2        -1
print(lista[-2:0])  # -> [6:0] -> []
print(lista[0:-2])  # 0:6 -> ['Radek', 'Tomek', 'Zenek', 'Ola', 'Aga', 'Kamil']

# range() - generowanie z zakresu
lista_15 = list(range(15))  # od 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(lista_15[0:15:2])  # [start:stop:krok] [0, 2, 4, 6, 8, 10, 12, 14] ostatni niewłącznie

print(list(range(0, 15, 2)))  # (start, stop, krok), [0, 2, 4, 6, 8, 10, 12, 14]

print(lista[::2])  # cała lista, co 2, ['Radek', 'Zenek', 'Aga', 'Adam']

print(lista[::-1])  # odwrócona lista
# ['Bogdan', 'Adam', 'Kamil', 'Aga', 'Ola', 'Zenek', 'Tomek', 'Radek']

# nadpisanie elementu w liście na wskazanym indeksie
# zmiana na oryginalnej liście
lista[3] = "Asia"
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Asia', 'Aga', 'Kamil', 'Adam', 'Bogdan']

# wstawienie elementu na wskazanym indeksie
lista.insert(1, "Ola")
print(lista)
# ['Radek', 'Ola', 'Tomek', 'Zenek', 'Asia', 'Aga', 'Kamil', 'Adam', 'Bogdan']

# usunięcie elementu z listy, po elemencie
lista.remove("Tomek")
print(lista)
# ['Radek', 'Ola', 'Zenek', 'Asia', 'Aga', 'Kamil', 'Adam', 'Bogdan']

# usunięci epo indeksie
# pop()
print(lista.pop(2))
# Zenek
zmienna = lista.pop(-1)
print("Zmienna:", zmienna)  # Zmienna: Bogdan
print(lista)

# ['Radek', 'Ola', 'Asia', 'Aga', 'Kamil', 'Adam']
lista.append("Radek")
print(lista)
lista.remove("Radek")  # usunie pierwszy napotkany
print(lista)
# ['Ola', 'Asia', 'Aga', 'Kamil', 'Adam', 'Radek']

# sprawdzenie indexu dla danego eleemntu

print(lista.index("Asia"))  # index 1

a = 1
b = 3
a = b
print(f"{a=}, {b=}")
# a=3, b=3
b = 9
print(f"{a=}, {b=}")  # a=3, b=9

lista_2 = lista  # odpowiednik a = b?, kopia referencji, adresu
lista_copy = lista.copy()  # kopia elementów listy
print(lista)
print(lista_2)
# ['Ola', 'Asia', 'Aga', 'Kamil', 'Adam', 'Radek']
# ['Ola', 'Asia', 'Aga', 'Kamil', 'Adam', 'Radek']
lista.clear()  # usunięcie elementów z listy o nazwie lista
print(lista)  # []
print(lista_2)  # []
print(lista_copy)  # ['Ola', 'Asia', 'Aga', 'Kamil', 'Adam', 'Radek']
print(id(lista))  # 2286828692032
print(id(lista_2))  # 2286828692032
print(id(lista_copy))  # 2286831271680

liczby = [54, 999, 34, 12.34, 567]
print(liczby)
print(type(liczby))  # <class 'list'>

liczby.sort()
print(liczby)  # [12.34, 34, 54, 567, 999]

liczby = [54, 999, 34, 12.34, 567, "A"]
print(type(liczby))  # <class 'list'>

# liczby.sort()
# TypeError: '<' not supported between instances of 'str' and 'int'

print(lista_copy)
# ['Ola', 'Asia', 'Aga', 'Kamil', 'Adam', 'Radek']
lista_copy.sort()
print(lista_copy)
# ['Adam', 'Aga', 'Asia', 'Kamil', 'Ola', 'Radek']

lista_copy.sort(reverse=True)
print(lista_copy)
# ['Radek', 'Ola', 'Kamil', 'Asia', 'Aga', 'Adam']

lista_copy.reverse()
print(lista_copy)
# ['Adam', 'Aga', 'Asia', 'Kamil', 'Ola', 'Radek']

liczby[3] = 666
print(liczby[0:3])
print(liczby[-2])
print(liczby)
# [54, 999, 34]
# 567
# [54, 999, 34, 666, 567, 'A']

# rozpakowanie sekwencji
tekst = "Pyth on."
lista1 = list(tekst)
print(lista1)  # ['P', 'y', 't', 'h', ' ', 'o', 'n', '.']

lista2 = [tekst]
print(lista2)  # ['Pyth on.']

krotka = tuple(lista_copy)
print(type(krotka))
print(krotka)
# <class 'tuple'>
# ('Adam', 'Aga', 'Asia', 'Kamil', 'Ola', 'Radek')
