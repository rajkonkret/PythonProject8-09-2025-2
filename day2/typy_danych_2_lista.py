# kolekcje

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
