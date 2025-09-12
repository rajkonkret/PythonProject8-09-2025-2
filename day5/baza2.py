# baza danych - system przechowywania danych
# silnik - mechanizm zarzadznai danymi w bazie danych
# sql, nosql
# sqlite, mysql, postregress, oracle, mssql
import sqlite3

try:
    conn = sqlite3.connect('baza_sqlite.db')
    c = conn.cursor()
    print('Baza danych została utworzona')

    query = """
    CREATE TABLE IF NOT EXISTS developers(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    salary REAL NOT NULL);
    """

    # c.execute(query)
    # conn.commit()

    insert = """
    INSERT INTO developers (id,name,email,salary) VALUES (1,'radek','rajkonkret.rajkonkret.pl', 10000);
    """
    # c.execute(insert)
    # conn.commit()

    select = """
    SELECT * FROM developers;
    """
    for row in c.execute(select):
        print(row)  # (1, 'radek', 'rajkonkret.rajkonkret.pl', 10000.0)

    update = """
    UPDATE developers SET salary=20000 WHERE id=1;
    """
    # c.execute(update)
    # conn.commit()

    delete = """
    DELETE FROM developers WHERE id=1;
    """
    c.execute(delete)
    conn.commit()
except sqlite3.Error as e:
    print("Bład połączenia z bazą:", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
# Baza danych została utworzona
# Połączenie zostało zamknięte
