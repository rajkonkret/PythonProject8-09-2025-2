# get
import requests

# z jsonów w pythonie robimy słownik
url = "https://api.nbp.pl/api/exchangerates/rates/A/eur/?format=json"

response = requests.get(url)
print(response)  # <Response [200]>
# 2xx ok
# 3xx warningi, przekierowania
# 4xx - błedy po stronnie użutkownika, 404
# 5xx - błędy po stronie serwera 500 Internal Server Error

print(response.text)
data = response.json()  # tworzymy słownik z jsona
print(data)
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
#  'rates': [{'no': '177/A/NBP/2025', 'effectiveDate': '2025-09-12', 'mid': 4.2593}]}
print(type(data))  # <class 'dict'>

print(data['rates'])  # [{'no': '177/A/NBP/2025', 'effectiveDate': '2025-09-12', 'mid': 4.2593}] jeden słownik w liście
print(data['rates'][0])  # {'no': '177/A/NBP/2025', 'effectiveDate': '2025-09-12', 'mid': 4.2593} słownik
print(data['rates'][0]['mid'])  # 4.2593
