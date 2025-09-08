# PEP8 - zasady czystego kodu w pythonie
import sys

print()  # wypisz/wydrukuj
# Process finished with exit code 0 program zakończył się bez błedu
# ctrl alt l - formatowanie wg PEP8
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
# ctrl d - duplikacja linii
print('Radek')  # Radek
# ctrl / - komentarz
# print('Radek")
# C:\Users\CSComarch\PycharmProjects\PythonProject8-09-2025-2\.venv\Scripts\python.exe C:\Users\CSComarch\PycharmProjects\PythonProject8-09-2025-2\day1\pierwszy.py
#   File "C:\Users\CSComarch\PycharmProjects\PythonProject8-09-2025-2\day1\pierwszy.py", line 15
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 15)
#
# Process finished with exit code 1
print('Dalsza częśc programu')
# Dalsza częśc programu

print("Radek \"Radek\"")  # \ znak ucieczki

# type() - sprawdzanie typu danych
print(type("Radek"))  # <class 'str'>, string, dane tekstowe

print("39" + "39")  # 3939 , łączy teksty, konkatenacja

print(39 + 39)  # 78
print(type(39))  # <class 'int'>, integer, liczby całkowite

print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)

# print("39" + 39)
# TypeError: can only concatenate str (not "int") to str

# musiamy jawnie rzutować
print(int("39"))  # rzutowanie(zamiana) na int
print(int("39") + 39)  # 78

print("Radek" + str(39))  # str() - rzutowanie na str
# Radek39

print(5 * "4")  # 44444
print(168 * "35")
# 353535353535353535353535353
# 53535353535353535353535353535
# 35353535353535353535353535353535
# 3535353535353535353535353535353535353
# 53535353535353535353535353535353535353
# 535353535353535353535353535353535353535353535353535353
# 53535353535353535353535353535353535353535353535353535353535353535
# 353535353535353535353535353535353535353535353535353535
print(168 * 35)  # 5880

# print(int("A"))
# ValueError: invalid literal for int() with base 10: 'A'

print(int(168) * int("35"))  # 5880

# zmienna - pudełko na dane
# snake_case
# nazwa zmiennej powinna podpowiadać co ma zawierać zmienna

name = "Radek"
a = "Radek"
print(name)  # wypisze zawartość zmiennej, 5880
# Radek
print(type(name))  # <class 'str'>

# typowanie dynamicznie
name = "Radek"
print(name + "Kowalski")  # RadekKowalski
print(type(name))  # <class 'str'>
# print(name + 90) # TypeError: can only concatenate str (not "int") to str
name = 90
print(name)
print(type(name))  # <class 'int'>

# name = 90Radek

# to jest podpowiedź typów
name: str = "Radek"
print(name)
name = 90
print(name)

age = 90
print(age)  # 90

# mypy
# pip install mypy
# cd .\day1\
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProject8-09-2025-2\day1> mypy .\pierwszy.py
# pierwszy.py:86: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# pierwszy.py:93: error: Name "name" already defined on line 75  [no-redef]
# pierwszy.py:95: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 3 errors in 1 file (checked 1 source file)
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProject8-09-2025-2\day1>