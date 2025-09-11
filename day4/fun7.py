def connect(**opcje):  # ** dowolna ilosć argumentów nazwanych
    print(opcje)


connect()
connect(a=100)  # {'a': 100}


def all_args(*args, **kwargs):
    print(args, kwargs)


all_args()  # () {}
all_args(1, 2, 3, 4, 5, 6, 7)  # (1, 2, 3, 4, 5, 6, 7) {}
all_args(a=10, b=10, c=3, d=78, name="Radek")
# () {'a': 10, 'b': 10, 'c': 3, 'd': 78, 'name': 'Radek'}

all_args(1, 2, 3, name="Radek")  # (1, 2, 3) {'name': 'Radek'}

# SyntaxError: positional argument follows keyword argument
# all_args(name="Radek", 1, 2)
