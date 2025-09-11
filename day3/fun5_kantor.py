# stworzyc funkcję kantor
# ma miec dwie funkcje wew: usd, eur
# w zależności od parametru ma wrócij jedną z tych funkcji
# przekazenie kwoty do funkcji wew
def kantor(waluta):
    def usd(kwota=0):
        print(f"Zamiana {kwota} usd na {kwota * 3.63} pln")

    def eur(kwota=0):
        print(f"Zamiana {kwota} eur na {kwota * 4.26} pln")

    if waluta == "eur":
        return eur
    else:
        return usd


kantor_usd = kantor("usd")  # dostaniemy adres funkcji
kantor_usd()  # uruchomienie funkcji kantor i w  niej usd
kantor_usd(1000)
# Zamiana 0 usd na 0.0 pln
# Zamiana 1000 usd na 3630.0 pln
kantor_eur = kantor("eur")
kantor_eur(1000)  # Zamiana 1000 eur na 4260.0 pln
