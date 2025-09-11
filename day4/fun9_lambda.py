# funkcja lambda
# skrócony zapis funkcji
# domyślnie lambda zwraca wynik (return)
# funkcja anoimowa

def odejmij(a, b):
    return a - b


print(odejmij(10, 8))  # 2

odejmij2 = lambda a, b: a - b  # domyślnie posiada return
print(odejmij2(10, 8))  # 2

# przerobic na lambdę
# def oblicz_vat(kwota, vat=23):
#     return kwota * (100 + vat) / 100

oblicz_vat = lambda kwota, vat=23: kwota * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
# 1230.0
# 1080.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")

print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

lista = [1, 2, 34, 24, 50, 67, 80, 100, 200, 500]

# mapowanie danych
l = []
for i in lista:
    l.append(i * 2)
print(l)  # [2, 4, 68, 48, 100, 134, 160, 200, 400, 1000]

print([i * 2 for i in lista])


# [2, 4, 68, 48, 100, 134, 160, 200, 400, 1000]

def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))

print(l2)  # [2, 4, 68, 48, 100, 134, 160, 200, 400, 1000]

# map() - wykonuje funkcje na lelementach kolekcji
# funkcja wyższego rzędu - jako argument przyjmuje inną funkcję

print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 68, 48, 100, 134, 160, 200, 400, 1000]

# lambda jako funkcja anonimowa - bez nazwy
# uzycie lambdy w miejscu deklaracji
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 0.5, lista))}")
# Zastosowanie map(): [2, 4, 68, 48, 100, 134, 160, 200, 400, 1000]
# Zastosowanie map(): [4, 8, 136, 96, 200, 268, 320, 400, 800, 2000]
# Zastosowanie map(): [0.5, 1.0, 17.0, 12.0, 25.0, 33.5, 40.0, 50.0, 100.0, 250.0]

# filtrowanie danych
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)
print(l3)  # [1, 2]

# filter()
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")  # Zastosowanie filter(): [1, 2]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 30, lista))}")  #
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 300, lista))}")  #
# Zastosowanie filter(): [34, 50, 67, 80, 100, 200, 500]
# Zastosowanie filter(): [1, 2, 34, 24, 50, 67, 80, 100, 200]

# x > 3 i x < 200
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3 and x < 200, lista))}")
# Zastosowanie filter(): [34, 24, 50, 67, 80, 100]
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 200, lista))}")
