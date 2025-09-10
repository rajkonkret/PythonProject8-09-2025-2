# od pythona 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programowania")

match lang:
    case "python":
        lista.append("Znam Pythona")
    case "java":
        lista.append("Znam Jave")
    case _:  # odpowiednik else
        print("Nie znam takiego języka")

print(lista)
# Podaj znany Ci język programowaniajava
# ['Znam Jave']
# Nie znam takiego języka
# []
