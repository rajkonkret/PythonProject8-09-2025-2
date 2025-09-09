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

podatek = 0
zarobki = int(input("Podaj zarobki"))

if zarobki < 10_000:
    podatek = 0
elif zarobki < 40_000:
    podatek = 0.2
elif zarobki < 100_000:
    podatek = 0.4
else:
    podatek = 0.9

print(f"Podatek wynosi {zarobki * podatek} pln")
# podatek 0.2 od 10_000 do 39_999
