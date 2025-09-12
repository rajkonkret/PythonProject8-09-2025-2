# dekoratory
# funkcje które jako argumet przyjmuja inne funkcje
# wykorzystuje zasadę funkcji wewnętrznej
def dekor(func):
    def wew():  # funkcja wrapper
        print("Dekorujemy")
        return func()  # zwracamy wynik funkcji dekorowanej

    return wew  # zwracamy adres funkcji wew


@dekor
def hej():
    print("Hej")


hej()


# bez dekoratora
# Hej
# z dekoratorem o nazwie dekor
# Dekorujemy
# Hej

# zrobic dekorator, który zamienia wynik funkcji na duże litery

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper  # adres funkcji wewnętrznej


@uppercase_decorator
def greeting():
    return "Hello World!"


print(greeting())  # Hello World!
# po uzyciu dekoratora
# HELLO WORLD!
