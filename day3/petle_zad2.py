dictionary = {'imie': "Radek", 'nzwisko': "Kowalski"}
print(type(dictionary))  # <class 'dict'>

# wyswietli klucze
for i in dictionary:
    print(i)
# <class 'dict'>
# imie
# nzwisko

for k in dictionary.keys():
    print(k)
# imie
# nzwisko

# wypisanie wartości
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wypisze pary
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nzwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nzwisko => Kowalski
#  sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.\

for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nzwisko=>Kowalski
for k, v in dictionary.items():
    print(k, v, sep="=>", end="<==>")
# imie=>Radek<==>nzwisko=>Kowalski<==>
print("Radek")  # imie=>Radek<==>nzwisko=>Kowalski<==>Radek
print("Tomek")  # nowa linia
# imie=>Radek
# nzwisko=>Kowalski
# imie=>Radek<==>nzwisko=>Kowalski<==>Radek
# Tomek

pol_ang = {'pies': "dog", 'kot': "cat", 'dach': "roof"}
ang_pol = {}
for k, v in pol_ang.items():
    ang_pol[v] = k
print(ang_pol)  # {'dog': 'pies', 'cat': 'kot', 'roof': 'dach'}

print({v: k for k, v in pol_ang.items()})
# {'dog': 'pies', 'cat': 'kot', 'roof': 'dach'}
