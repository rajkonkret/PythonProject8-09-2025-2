# działania z plikami
# filehandler - rura do pliku
# context manager
# with - context manager w pythonie

#     ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open("test.log", "w", encoding="utf-8") as fh:
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jescze jedno\n")

# # FileExistsError: [Errno 17] File exists: 'test.log'
# with open('test.log', "x", encoding="utf-8") as f:
#     f.write("Powitanie")

# nadpisze istniejący plik
with open("test.log", "w", encoding="utf-8") as file:
    file.write("Nowe dane\n")

with open('test.log', "a", encoding="utf-8") as f:
    f.write("Dopisane\n")
    f.write("Dopisane\n")
    f.write("Dopśisane\n")

with open("test.log", "r", encoding="utf-8") as file:
    lines = file.read()

print(lines)
# Nowe dane
# Dopisane
# Dopisane
# Nowe dane
# Dopisane
# Dopisane
# Dopśisane
