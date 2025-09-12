# generatory - funkcje zwracające kolejne wyniki
# nie przechowuje kolejnych wyników
# podstawia w kolejności (dostęp sekwencyjny)
# efektywne zarządzanie pamięcią
# leniwe - generowaie - dane dostarczane są tylko wtedy kiedy są potrzebne

def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


# 0
# 1
# 4
# 9
# 16

# generator
def kwadrat(n):
    for x in range(n):
        yield x ** 2  # wykonuje operacje, zwraca wynik, pamięta który jest następny


print(kwadrat(5))  # <generator object kwadrat at 0x000001C68821A9B0>
kwa = kwadrat(5)
print(type(kwa))  # <class 'generator'>

# wyswietla koljny pojedynczy element
print(next(kwa))
print(next(kwa))
print(next(kwa))
# 0
# 1
# 4
print("Zrób cokolwiek")
lista = []
lista.append("Radek")
print(lista)
print("Tekst")
print(next(kwa))  # 9
print(next(kwa))  # 16


# generator wyczerpał dane
# print(next(kwa))  # StopIteration

# generator bez końca
def counter(start=0):
    n = start
    while True:
        yield n
        n += 1


c = counter()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))


def counter_down(min):
    count = min
    while count > 0:
        yield count
        count -= 1


c2 = counter_down(10)
print(next(c2))
print(next(c2))
print(next(c2))

# wyciąga wszystkie dane z generatora
for i in counter_down(10):
    print(i)


def counter_2(start=0):
    n = start
    while True:
        result = yield n
        print(result)
        if result == "q":
            break
        n += 1


c3 = counter_2(10)
print(next(c3))
print(next(c3))
print(next(c3))
print(next(c3))

c3.send("OK")
print(next(c3))

try:
    c3.send("q")
except StopIteration as e:
    print("koniec danych:", e)

# None
# 13
# OK
# None
# 15
# q
# koniec danych:
