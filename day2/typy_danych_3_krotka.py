# krotka - tuple - kolekcja niemutowalna, tylko do odczytu
# pozwala efektywniej zarządzać pamięcia
# krotka jednoelementowa - stała, szczególny przykład zmiennej

tupla_imiona = "Zanek", "Marek", "Tomek", "Radek", "Ania"
print(type(tupla_imiona))  # <class 'tuple'>
print(tupla_imiona)  # ('Zanek', 'Marek', 'Tomek', 'Radek', 'Ania')

tupla_liczby = 43, 55, 22.34, 11, 200
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

# nawias pełni role pomocniczą
tupla_liczby = (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

# tuple jedoelementową
tupla_jeden = 45,
print(tupla_jeden)  # (45,)
print(type(tupla_jeden))  # <class 'tuple'>

# PEP8 zaleca tuple jedoelementową tworzyć z nawiasem
tupla_jeden = (45,)
print(type(tupla_jeden))
print(tupla_jeden)

# 36.6 36,6
# tupla jest niemutowalna,  nie można zmienic
# tupla_jeden[0] = 123
# TypeError: 'tuple' object does not support item assignment

# usunięcie całej tupli
del tupla_jeden

# po usunięciu tupla nie istnieje
# NameError: name 'tupla_jeden' is not defined
# print(tupla_jeden)

print(tupla_imiona.index("Radek"))  # index numer 3
print(tupla_imiona.count("Radek"))  # jet 1 element

print(len(tupla_imiona))  # długośc 5

# rozpakowanie tupli
tup = 1, 2
print(type(tup))  # <class 'tuple'>

a, b = 1, 2
print(f'{a=}, {b=}')  # a=1, b=2

a, b = tup
print(f'{a=}, {b=}')  # a=1, b=2

tup_2 = 1, 2, 3
# a, b = tup_2
# ValueError: too many values to unpack (expected 2)
a, *b = tup_2  # * - worek na pozostałe dane
print(a, b)  # 1 [2, 3]

print(tupla_imiona)
print(len(tupla_imiona))
# ('Zanek', 'Marek', 'Tomek', 'Radek', 'Ania')
# 5
# name1,name2,name3
name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)  # Zanek Marek ['Tomek', 'Radek', 'Ania']

*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)  # ['Zanek', 'Marek', 'Tomek'] Radek Ania

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)
# Zanek ['Marek', 'Tomek', 'Radek'] Ania

# sortowanie krotki zwróci liste
print(sorted(tupla_imiona))
# ['Ania', 'Marek', 'Radek', 'Tomek', 'Zanek']
print(tupla_imiona)  # ('Zanek', 'Marek', 'Tomek', 'Radek', 'Ania')
# krotka się nie zmieniła
