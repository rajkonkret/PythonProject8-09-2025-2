# pętla - pozwala wielokrotnie wykonac fragment kodu
# for  - pętla iteracyjna
import random

for i in range(5):  # od 0 do 4
    print(i)
# 0
# 1
# 2
# 3
# 4

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # niema zmienna
    print("Test podłoga")
    print(_)

for i in range(5):
    print(i + 2)
    print(i * 2)

# przerobic lotto na pętle
lista_kule = list(range(1, 50))
lista_wyn = []
for _ in range(6):  # od 0 do 5
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    # print(wyn)
    lista_wyn.append(wyn)

print(lista_wyn)  # [22, 41, 11, 25, 12, 37]

for i in range(10):  # modulo, reszta z dzielenia
    if i % 2 == 0:
        print(i, "parzysta")

# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

lista3 = []
for j in range(10):
    if j % 2 == 0:
        lista3.append(j)
print(lista3)  # [0, 2, 4, 6, 8]

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista3:  # weźmie wszystkie elementy tej listy
    if c > 4:
        print(c, "Większe od 4")
    elif c == 4:
        print(c, "Równe 4")
    else:
        print(c, "Mniejsze od 4")
# 0 Mniejsze od 4
# 2 Mniejsze od 4
# 4 Równe 4
# 6 Większe od 4
# 8 Większe od 4

for i in range(0, 10, 2):  # (start, stop, krok), co drugi
    print(i)
# 0
# 2
# 4
# 6
# 8

for i in range(-10, 0):
    print(i)
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1
for i in range(10, 0, -2):  # krok ujemny, wstecz
    print(i)
# 10
# 8
# 6
# 4
# 2

for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
        print(c)  # tylko dla c równego 2
    print("Wykona się za każdym przejsciem pętli")
print("po zakończeniu pętli")

imiona = ["Radek", "Tomek", "Agata", "Marek"]
print(imiona)  # ['Radek', 'Tomek', 'Agata', 'Marek']
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Agata
# Marek

# 0 Radek

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Marek

for i in range(len(imiona)):
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Marek

# enumerate() - zwraca numer i element
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Agata')
# (3, 'Marek')

for i, p in enumerate(imiona):
    print(i, p)
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Marek

for i, p in enumerate(imiona, start=1):  # start numeracji od 1
    print(i, p)
# 1 Radek
# 2 Tomek
# 3 Agata
# 4 Marek

imiona = ["Radek", "Tomek", "Agata", "Marek", "Ewa"]
wiek = [44, 56, 23, 34]

# Radek 44
# for p in imiona:
#     print(p, wiek[imiona.index(p)])
# IndexError: list index out of range
# Radek 44
# Tomek 56
# Agata 23
# Marek 34

# zip() - łączy kolekcje
for i in zip(imiona, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 56)
# ('Agata', 23)
# ('Marek', 34)
for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 44
# Tomek 56
# Agata 23
# Marek 34

# 0 Radek 44

for i in enumerate(zip(imiona, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Tomek', 56))
# (2, ('Agata', 23))
# (3, ('Marek', 34))
a, b = (3, ('Marek', 34))
print(a, b)  # 3 ('Marek', 34)
c, d = ('Marek', 34)
print(a, c, d)  # 3 Marek 34
(a, (c, d)) = (3, ('Marek', 34))
for i, (o, w) in enumerate(zip(imiona, wiek)):
    print(i, o, w)
# 0 Radek 44
# 1 Tomek 56
# 2 Agata 23
# 3 Marek 34