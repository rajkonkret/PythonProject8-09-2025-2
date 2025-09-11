def all_params(a, b, /, c=42, d=256):
    print(f"{a}, {b}")
    print(f"{c}, {d}")


# TypeError: all_params() missing 2 required positional arguments: 'a' and 'b'
# all_params()
all_params(1, 2)  # 1, 2
all_params(1, 2, 3, 4)
# 1, 2
# 3, 4
# TypeError: all_params() got some positional-only arguments passed as keyword arguments: 'a, b'
# / oddziela argumenty pozycyjne (positional-only) od pozostałch
# all_params(a=5, b=6, c=7, d=90)
all_params(5, 6, c=7, d=90)
# 5, 6
# 7, 90

print(50 * "_")


def all_params2(a, b, /, c=42, *args, d=256, **kwargs):
    print(f"{a}, {b}")
    print(f"{c}, {d}")
    print(f"{args}")
    print(f"{kwargs}")


all_params2(1, 2)
all_params2(1, 2, 3)
all_params2(1, 2, c=3)
all_params2(1, 2, c=3, d=5)
all_params2(1, 2, 3, 4, 4, 5, 6, 7)  # (4, 4, 5, 6, 7)
# d musi byc po nazwie bo jest po *args(4, 4, 5, 6, 7)
all_params2(1, 2, 3, 4, 4, 5, 6, 7, d=90)  # (4, 4, 5, 6, 7)
all_params2(1, 2, 3, 4, 4, 5, 6, 7, d=90, e=88, name="Rdek")
# 1, 2
# 3, 90
# (4, 4, 5, 6, 7)
# {'e': 88, 'name': 'Rdek'}
all_params2(1, 2, 3, 4, 4, 5, 6, 7, a=888, d=90, e=88, name="Rdek")
# 1, 2
# 3, 90
# (4, 4, 5, 6, 7)
# {'a': 888, 'e': 88, 'name': 'Rdek'}
