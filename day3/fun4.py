# funkcja wewnętrzna, zagnieżdżona
# dekorator - wykorzystuje zasadę funkcji zagniezdzonej

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    # fun2() zwraca wynik dziłania funkcji a nie adres

    return fun2  # zwracamy adres funkcji, referencję


fun1()  # To jest fun1
print(type(fun1))  # <class 'function'>
print(fun1)  # <function fun1 at 0x0000020C96F91440>
xFun = fun1()
print(type(xFun))  # <class 'function'>
print(xFun)  # <function fun1.<locals>.fun2 at 0x0000028AE5B23D80>
xFun()  # To jest fun2
