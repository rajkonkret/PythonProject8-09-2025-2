import random

# działania na liczbach losowych

"""Return random integer in range [a, b], including both end points."""
print(random.randint(1, 100))  # int w zakresie od 1 do 100 (z prawej zamknięty)
print(random.randrange(1, 100))  # int w zakresie od 1 do 99
print(random.randrange(10))  # ind od 0 do 9

print(random.random())  # float 0.11417300884148718 od 0 do 0.9999999
print(random.random() * 7)  # float 0.11417300884148718 od 0 do 6.9999999

lista = [67, 45, 32, 68, 90, 42, 69]
print(random.choice(lista))  # wylosowany element z listy, 45

lista_kule = list(range(1, 50))
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)  # 25

print(random.choices(lista_kule, k=6))  # [34, 10, 8, 36, 33, 33], z powtózeniami
print(random.sample(lista_kule, k=6))  # bez powtórzeń
print(random.sample(lista_kule, 6))  # bez powtórzen
# [47, 28, 24, 17, 6, 1]
# [25, 14, 49, 10, 36, 41]
