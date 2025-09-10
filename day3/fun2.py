# funkcje zwracające wynik
# kończy się return

def dodaj(a, b):
    return a + b


def odejmij(a, b=0, c=0):
    return a - b - c


print(dodaj(5, 9))  # 14
wynik = dodaj(4, 90)
print("Wynik:", wynik)  # Wynik: 94

# pozycyjnie, po nazwie, mieszane
print(odejmij(5, 8, 90))  # -93
print(odejmij(c=5, b=8, a=90))  # 77
print(odejmij(5, b=8, c=90))  # -93


def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100


print(oblicz_vat(1000))
print(oblicz_vat(1000, 15))
print(oblicz_vat(vat=8, kwota=1000))
# 1230.0
# 1150.0
# 1080.0

zm = oblicz_vat(1000)
if zm == 1230:
    print("OK")  # OK

print(dodaj(5, 7) + odejmij(5, 6))  # 11
