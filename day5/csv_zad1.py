# csv - dane oddzielone znakiem podziału
# imię,opis,ocena
# Andrzej Nowak,fajny,4
# "Jan Wiśniewski","fajny","2"
# Kowalski,"wiecznie pyta ""która godzina"", ale może być",5

import csv

# csv - bilbioteka do działania z plikami csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['radek', 'coe', "3", 0]

dict_dane = dict(zip(fields, row))
print(dict_dane)
# {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': 0}

filename = "records.csv"
# newline="" ominięcie pustych lini
with open(filename, "w", newline="") as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

filename = "records_dict.csv"
with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()  # nazwy kolumn
    csvwriter.writerow(dict_dane)

products = [
    {"sku": 1, "exp_date": "today", "price": 120},
    {"sku": 2, "exp_date": "today", "price": 200},
    {"sku": 3, "exp_date": "tommorow", "price": 20.50},
    {"sku": 4, "exp_date": "today", "price": 5.20},
    {"sku": 5, "exp_date": "today", "price": 1200},
]

list_product = [key for key in products[0]]
filename = "records_discount.csv"
with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=list_product, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(products)  # writerows - zapis listy sowników
