# baza danych - system przechowywania danych
# silnik - mechanizm zarzadznai danymi w bazie danych
# sql, nosql
# sqlite, mysql, postregress, oracle, mssql
import sqlite3

try:
    conn = sqlite3.connect('baza_sqlite.db')
    c = conn.cursor()
    print('Baza danych została utworzona')
except sqlite3.Error as e:
    print("Bład połączenia z bazą:", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
# Baza danych została utworzona
# Połączenie zostało zamknięte
