import shutil
from pathlib import Path

base_path = Path("ops_example")
base_path2 = Path("ops_example/D")

print(base_path)
print(base_path2)
# ops_example
# ops_example\D

# jeśli katalog istnieje to go usuniemy
if base_path.exists() and base_path.is_dir():
    shutil.rmtree(base_path)

# tworzenie katalogu
base_path.mkdir()

path_b = base_path / "A" / "B"
path_c = base_path / "A" / "C"
path_d = base_path / "A" / "D"

# brak katalogu A powuduje, ż enie można utworzyć w nim B
# FileNotFoundError: [WinError 3] System nie może odnaleźć określonej ścieżki: 'ops_example\\A\\B'
# path_b.mkdir()

# musimy jawnie powiedzieć, ze ma stowrzyc brakujące katalogi
path_b.mkdir(parents=True)

# katalo c ju zsię stworzy normalnie bo istnieje już A
path_c.mkdir()

# tworzenie plików
for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(path_b / filename, "w", encoding="utf=8") as stream:
        stream.write(f"Jakaś treść w pliku {filename}")

# przeniesienie katalogu
shutil.move(path_b, path_d)

# zmiana nazwy pliku
ex1 = path_d / 'ex1.txt'
ex1.rename(ex1.parent / 'ex1renmed.log')

# kopiwanie pliku
ex1 = path_d / "ex1renmed.log"
docelowy = path_c
shutil.copy(ex1, docelowy)

# tworzenie ścieżek windows
# C:\Users\CSComarch\PycharmProjects\PythonProject8-09-2025-2\day5\ops_example\A\D\ex1renmed.log
# C:\\Users\\CSComarch\\PycharmProjects\\PythonProject8-09-2025-2\\day5\\ops_example\\A\\D\\ex1renmed.log

# r - raw
# r"C:\Users\CSComarch\PycharmProjects\PythonProject8-09-2025-2\day5\ops_example\A\D\ex1renmed.log"
