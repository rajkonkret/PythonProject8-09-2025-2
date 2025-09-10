# funkcja - wydzielony fragment programy, moży użyc w dowolnym momncie
# funkcja musi najpierw zostac zadeklarowana
# żeby funkjca się wykonała musi być uruchomiona

a = 8
b = 6


# deklaracja funkcji
def dodaj():  # funkcja bezargumentowa
    # użył wartości z globalnego scopa
    print(a + b)


def dodaj2(a, b):
    # zadeklarowane lokalne zmienne
    print(a + b)


# pozwala zasymulować przeciążanie funkcji liczbą argumentów
def odejmij(a, b, c=0):  # argument c z wartością domyslną
    print(a - b - c)


# użycie funkcji (wywołanie)
# nazwa funkcja i nawiasy ()
dodaj()  # 14
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
# argumenty pozycyjne
dodaj2(10, 67)  # 77

odejmij(1, 2)  # c=0,-1
odejmij(1, 2, 5)  # -6

# po nazwie
odejmij(c=9, a=9, b=123)  # -123
odejmij(b=45, a=90)  # 45

# mieszanne
odejmij(1, 2, c=90)  # -91

# odejmij(c=90, 1, 2) # SyntaxError: positional argument follows keyword argument

# funkcja nie zwraca wyniku
# print(dodaj() + dodaj2(4, 5))
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
