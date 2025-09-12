import pandas

# pip install pandas

data = pandas.read_csv('records.csv')
print(data)
#      name branch  year  cgpa
# 0  radek    coe     3     0

print(data.values)  # [['radek' 'coe' 3 0]]
print(data.columns)  # Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(data.items)
# <bound method DataFrame.items of     name branch  year  cgpa
# 0  radek    coe     3     0>

data = pandas.read_csv("records_discount.csv", delimiter=";")
print(data)
#    sku  exp_date   price
# 0    1     today   120.0
# 1    2     today   200.0
# 2    3  tommorow    20.5
# 3    4     today     5.2
# 4    5     today  1200.0
