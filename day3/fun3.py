a = 10
b = 10


def dodaj():
    a = 7  # lokalna zmienna
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)  # użyje globalnych


def dodaj3():
    global a  # a ma byc uzyte globalne wewnątrz funkcji
    a = 9
    b = 30
    print(a+ b)

print(f"Wartość a z góry: {a=} (globalna)")  # Wartość a z góry: a=10 (globalna)
dodaj()  # 15 wykonane na lokalnych zmiennych
print(f"Wartość a z góry: {a=} (globalna)")  # Wartość a z góry: a=10 (globalna)
dodaj2()  # 20 - wykonało się na globalnych wartosciach
print(f"Wartość a z góry: {a=} (globalna)")  # Wartość a z góry: a=10 (globalna)
dodaj3() # 39
print(f"Wartość a z góry: {a=} (globalna)")  # Wartość a z góry: a=9 (globalna)
