# wyjątki - błędy w działąniu programu


# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonProject8-09-2025-2\day3\wyjatki.py", line 4, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
#
# Process finished  with exit code 1
lista = []

try:
    # print(5 / 0)
    # print("A" * "23")
    # int("A")
    # print(lista[10])
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dzielimy przez zero")
except TypeError:
    print('Błąd typu')
except ValueError:
    print('Bład wartości')
except Exception as e:
    print("Błąd:", e)
else:  # tylko gdy nie ma błedu
    print('Wynik:', wynik)
finally:
    print("Wykona się zawsze")

print('Program nadal działa')
# Nie dzielimy przez zero
# Program nadal działa
#
# Process finished with exit code 0
# Błąd typu
# Program nadal działa
#
# Process finished with exit code 0
# Błąd: list index out of range
# Program nadal działa
