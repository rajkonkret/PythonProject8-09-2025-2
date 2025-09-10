from datetime import datetime, date, timedelta

today = date.today()
print(today)  # 2025-09-10
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2025-09-10 12:27:34.219731

formated_date = datetime.now().strftime("%d/%m/%Y")
print(formated_date)  # 10/09/2025
print(type(formated_date))  # <class 'str'>

formated_time = datetime.now().strftime("%H:%M")
print(formated_time)  # 12:32

formated_time_12h = datetime.now().strftime("%I:%M %p")
print(formated_time_12h)  # 12:36 PM

# tommorow = today + 1
# TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tommorow = today + timedelta(days=1)
print(tommorow)  # 2025-09-11

products = [
    {"sku": 1, "exp_date": today, "price": 120},
    {"sku": 2, "exp_date": today, "price": 200},
    {"sku": 3, "exp_date": tommorow, "price": 20.50},
    {"sku": 4, "exp_date": today, "price": 5.20},
    {"sku": 5, "exp_date": today, "price": 1200},
]

for i in products:
    # print(i) # {'sku': 1, 'exp_date': datetime.date(2025, 9, 10), 'price': 120}
    # print(i['exp_date']) # 2025-09-10

    if i['exp_date'] != today:
        continue  # idz na początek pętli, weź kolejny element
    i['price'] *= 0.8  # price = price * 0.8
    print(f"""Price for sku {i['sku']}
is now {i['price']}""")
# Price for sku 1
# is now 96.0
# Price for sku 2
# is now 160.0
# Price for sku 4
# is now 4.16
# Price for sku 5
# is now 960.0