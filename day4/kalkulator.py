# napisać program kalkulator z wykorzystaniem pętli while True
# menu z dostępnymi opcjami
# pobrać wybraną opcję
# wyświetlić w sposób sforamtowy wynik dziłania
# obłużyć wyjątki
def dodaj(a, b):
    return a + b


def dzielenie(a, b):
    return a / b


while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)

    odp = input("Podja wybraną opcję")
    if odp == "5":
        break

    try:
        a = int(input("Podaj pierwszą liczbę"))
        b = int(input("Podaj drugą   liczbę"))

        if odp == "1":
            # print(f"Wynik {a} + {b} = {a + b}")
            print(f"Wynik {a} + {b} = {dodaj(a, b)}")
        elif odp == "2":
            print(f"Wynik {a} - {b} = {a - b}")
        elif odp == "3":
            print(f"Wynik {a} * {b} = {a * b}")
        elif odp == "4":
            print(f"Wynik {a} / {b} = {dzielenie(a, b)}")
        else:
            print("Błędna opcja menu")
    except ZeroDivisionError:
        print("Nie dziel przez zero!!!")
    except Exception as e:
        print("Bład:", e)
    finally:
        print("Podaj kolejną operację")

wyr = "5*7+9"
print(eval(wyr))  # 44
