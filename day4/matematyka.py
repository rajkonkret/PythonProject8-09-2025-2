import math
from itertools import zip_longest

print(math.pi)  # 3.141592653589793
print(math.sqrt(25))  # 5.0 -> float

angle_degree = 30
angle_radians = math.radians(angle_degree)
sin_value = math.sin(angle_radians)
print(f"sin({angle_degree}) = {sin_value}")
# sin(30) = 0.49999999999999994

angles = [0, 30, 45, 60, 90]
sin_values = [math.sin(math.radians(a)) for a in angles]

for a, s in zip(angles, sin_values):
    print(f"sin({a}) = {s:.2f}")
# sin(0) = 0.0
# sin(30) = 0.49999999999999994
# sin(45) = 0.7071067811865476
# sin(60) = 0.8660254037844386
# sin(90) = 1.0
# :.2f
# sin(0) = 0.00
# sin(30) = 0.50
# sin(45) = 0.71
# sin(60) = 0.87
# sin(90) = 1.00

imiona = ["Radek", "Tomek", "Agata", "Marek", "Ewa"]
wiek = [44, 56, 23, 34]

zipped = zip_longest(imiona, wiek, fillvalue=None)
print(zipped)  # <itertools.zip_longest object at 0x0000024826872B60> iterator

for item in zipped:
    print(item)
# ('Radek', 44)
# ('Tomek', 56)
# ('Agata', 23)
# ('Marek', 34)
# ('Ewa', None)

# tylko raz możemy wykorzystac dane
print(40 * "-")
for i, o in zipped:
    print(i, o)
# ----------------------------------------
