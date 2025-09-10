# while - pętla sterowana warunkiem

# pętla nieskonczona
# while True:
#     print("komunikat!")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerwanie pętli
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!

print(45 * "-")
print(licznik)
licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunika3")
# ---------------------------------------------
# 11
# Komunika3
# Komunika3
# Komunika3
# Komunika3
# Komunika3
# Komunika3
# Komunika3
# Komunika3
# Komunika3
# Komunika3

# password = input("Podaj hasło")
# while password != "secret":  # != - rózne
#     password = input("Podaj ponownie")
# print("Hasło poprawne")
# Podaj hasłoaaaaaa
# Podaj ponownieadafa
# Podaj ponowniexcefewfss
# Podaj ponowniesecret
# Hasło poprawne

lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")  # str
    # A string is numeric if all characters in the string are numeric
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))  # rzutowanie na int()

print(lista)  # ['1', '2', '3', '4', '5', '6', '7', '8', '910']
print(lista_int)  # [1, 2, 3, 4, 5]

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
while 5 in my_list:
    my_list.remove(5)
print(my_list)  # [1, 2, 3, 4, 6], usunła 5 i zachował kolenośc

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
print(dict.fromkeys(my_list))  # {1: None, 5: None, 2: None, 3: None, 4: None, 6: None}
print(list(dict.fromkeys(my_list)))  # [1, 5, 2, 3, 4, 6]
