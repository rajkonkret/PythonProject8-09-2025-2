# stworzyć funkcję obliczającą średnią

def srednia(name=None, *cyfry):  # dolna ilośc argumentów pozycyjnych
    print(cyfry)  # (1, 2, 3)
    count = len(cyfry)
    suma = 0
    suma_p = sum(cyfry)
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
        avg_p = suma_p / count
    except Exception as e:
        print("Błąd:", e)
    else:  # gdy nie ma błedu
        print(f"Średnia dla ucznia: {name}, wynosi:", avg)
        print(f"Średnia wynosi:", avg_p)
    finally:
        print("Następny uczeń")


srednia(1, 2, 3)
srednia()
# (1, 2, 3)
# Średnia wynosi: 2.0
# Średnia wynosi: 2.0
# Następny uczeń
# ()
# Błąd: division by zero
# Następny uczeń
srednia("Radek", 5, 6, 5, 6, 5, 4, 3, 5)
# C:\Users\CSComarch\PycharmProjects\PythonProject8-09-2025-2\.venv\Scripts\python.exe C:\Users\CSComarch\PycharmProjects\PythonProject8-09-2025-2\day4\fun6.py
# (2, 3)
# Średnia dla ucznia: 1, wynosi: 2.5
# Średnia wynosi: 2.5
# Następny uczeń
# ()
# Błąd: division by zero
# Następny uczeń
# (5, 6, 5, 6, 5, 4, 3, 5)
# Średnia dla ucznia: Radek, wynosi: 4.875
# Średnia wynosi: 4.875
# Następny uczeń
