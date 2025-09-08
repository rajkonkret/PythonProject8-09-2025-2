tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))

# Witaj Świecie
# <class 'str'>

# teksty są niemutowalne
tekst.upper()
print(tekst)  # Witaj Świecie
#  """ Return a copy of the string converted to uppercase. """
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE

print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie
print(tekst)  # Witaj Świecie

# Witaj Świecie
# 01234567890... indeksy numerowane 0

print(tekst[2])  # t, indeks numer2, pozycja 3

print(tekst.index("Ś"))  # indeks 6

print(tekst.count("i"))  # występuje 3 razy, 3
# nie piszemy x:, __start:, __end:
# z prawej strony  otwarty, bierze indeksy 0123
print(tekst.count("j", 0, 4))  # w tym zakresie występuje 0 razy

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usuniecie białych znaków, spacji przód, tył
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie'
print(type(encode_s))  # <class 'bytes'>
# b - typ bajtowy
# \xc5\x9a unicode znaku zapisany w formie szesnastkowej \x
print(encode_s.decode("utf-8"))  # Witaj Świecie

imie = "Radek"
# f - stringi sforamtowane
tekst_format = f"Mam na imię {imie} i lubię Pythona."
print(tekst_format)  # Mam na imię Radek i lubię Pythona.

tekst_format = f"\tMam na imię {imie}\n i lubię Pythona.\b"
print(tekst_format)
# "	Mam na imię Radek
#  i lubię Pythona"
# \t tabulator
# \n nowa linia
# \b backspace

starszy = "Witaj %s!"  # %s - w to miejsce oczekuje strinha
print(starszy % imie)  # Witaj Radek!

print("Witaj {}".format("Radek"))  # Witaj Radek

print("Witaj", imie)

print("""
    tekst
        wielolinijkowy""")
# "
#     tekst
#         wielolinijkowy"

# komentarz wielolinijkowy jest traktowany jako docstring
"""
Komentarz
 Linijkowy"""
