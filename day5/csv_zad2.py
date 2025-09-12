import csv

# filename = "records.csv"
filename = "records_discount.csv"

fields = []
rows = []

with open(filename, "r") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)  # ;

    # ponownie ustawiamy odczyt na początek pliku
    csv_f.seek(0)

    # csvreader = csv.reader(csv_f)
    # csvreader = csv.reader(csv_f, delimiter=";")
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)

    print(csvreader)  # <_csv.reader object at 0x000001EF63270A00>
    fields = next(csvreader)  # odczyt pierwszego wiersz, ustawienie odczytu na następny

    for row in csvreader:  # czyta od drugiego wiersza
        # print(row)
        rows.append(row)

print("Fields:", fields)
print("Rows:", rows)
# Fields: ['name', 'branch', 'year', 'cgpa']
# Rows: [['radek', 'coe', '3', '0']]
