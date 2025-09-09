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
print(lista[2:2]) # []
print(lista[2:3]) # ['Zenek']
