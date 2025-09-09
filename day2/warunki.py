# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zależności od warunku wykon ajeden lub drugi blok programu
# warunek musi zwracać typ  bool

odp = True
print(bool(odp))  # True

odp = False
# debugger, pułapka
if odp:
    # blok programu wykonywany gdy warunek jest spełniony
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
print("Dalsza częśc prograamu")
# Brawo
# Dalsza częśc prograamu

odp = "Radek"
print(bool(odp))  # True

if odp:
    print("Dane zostały wczytane")
# Dane zostały wczytane

if odp == "Radek":  # porównanie
    print("Jesteś Radek")
    # Jesteś Radek

odp = 0  # False
if odp:
    print("Działa")
else:  # w przeciwnym wypadku
    print("Zero -> False")
# Zero -> False

a = "Radek"
n = len(a)
if n > 3:
    print(f"Długość wynosi {n}, więcej niż 3")
# Długość wynosi 5, więcej niż 3

# walrus operator,  operator mors
if (n := len(a)) > 3:
    print(f"Długość wynosi {n}, więcej niż 3")

# podatek = 0
# zarobki = int(input("Podaj zarobki"))
#
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {zarobki * podatek} pln")
# # podatek 0.2 od 10_000 do 39_999
# ctrl /  - komentowanie

sum_zam = 150
if sum_zam > 100:
    rabat = 25
else:
    rabat = 0
print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

rabat = 25 if sum_zam > 100 else 0
print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

# zasymulujemy system zbierania logów
# zmienna przechowujący typ systemu
# console, email, inny
# console: "Stało się coś strasznego"
# email: "System email"
# jesli system email
# do listy błedów dodac tłumaczenie błedu
# zmienna przechowuje poziom błedu
# error, medium, inny
alert_system = "email"
error = "error"
lista_b = []
if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System email")
    if error == "error":
        lista_b.append("Krytyczny")
    elif error == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("Inny")

else:
    print("Inny system")

print(lista_b)
# System email
# ['Krytyczny']

# napisać test z....
# 3 pytania
# dodac punktację
punkty = 0
odp = input("Podaj rok Chrztu Polski")
if odp.strip() == '966':
    print("Prawidłowa odpowiedź")
    # punkty = punkty + 1
    punkty += 1
else:
    print("Błędna odpowiedź")
print(punkty)

odp = input("Podaj rok Chrztu Polski")
if odp.strip() == '966':
    print("Prawidłowa odpowiedź")
    punkty += 1
else:
    print("Błędna odpowiedź")

print(punkty)
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
