# słownik - para klucz - wartość
# {"user":"Radek", "wiek": 35}
# klucze nie mogą się powtarzac
# odpowiednik jsona

# pusty słownik
dictionary = {}
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary_1 = dict()
print(dictionary_1)  # {}
print(type(dictionary_1))  # <class 'dict'>

# dodanie eleemntu do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 48
print(dictionary)  # {'imie': 'Radek', 'wiek': 48}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 48])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 48)])

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 48}

# wypisanie wartości dla klucza
print(dictionary['imie'])
print(dictionary['imie'])
# Tomek
# Tomek

# print(dictionary['Imie'])
# KeyError: 'Imie'
print(dictionary["Imie".lower()])
print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "default"))  # default

name1 = "GROSS"
name2 = "groẞ"

print(name1.lower() == name2.lower())  # False
#    """ Return a version of the string suitable for caseless comparisons. """
print(name1.casefold() == name2.casefold())  # True

print(dictionary.get("imie"))  # True

dictionary.update({"data": "12-12-2027"})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 48, 'data': '12-12-2027'}

dict_small = {'x': 2}
print(dict_small)
dict_small.update([("y", 3), ("z", 8)])
print(dict_small)

# # input() - wprowadzanie danych do komputera
# tekst = input("Podaj imię")
# print(tekst)
# # Podaj imięRadek
# # Radek

# # napisac aplikację kalkulator
# # input zwraca stringa
# a = int(input('podaj pierwsza liczbę:'))
# b = input('podaj drugą liczbę:')
# print(int(a) + float(b))
# # podaj pierwsza liczbę:5
# # podaj drugą liczbę:6
# # 11.0

# napisać aplikację słownik pol-ang
pol_ang = {'pies': "dog", 'kot': "cat", 'dach': "roof"}
print("Znam takie słówka:", pol_ang.keys())
odp = input("Podaj słówko do przetłumaczenia:")
# print(pol_ang[odp.strip().casefold()])
print(pol_ang.get(odp.strip().casefold(), "Nie ma w słowniku!"))
# Znam takie słówka: dict_keys(['pies', 'kot', 'dach'])
# Podaj słówko do przetłumaczenia:Lew
# Nie ma w słowniku!