import requests

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
print(response)

print(response.text)

data = response.json()

print(data.keys())
# dict_keys(['categories', 'created_at', 'icon_url', 'id', 'updated_at', 'url', 'value'])

for k in data:
    print(k)
# categories
# created_at
# icon_url
# id
# updated_at
# url
# value

print(data['value'])
# see the picture on top that has Chuck Norris
# (' face on it? stare at it too long, and you will'
#  ' get a imaginary roundhouse kick to the face.)
print(data.get('value'))
# Chuck Norris can make a silk purse out of a sow's ear.

response_img = requests.get(data["icon_url"])
with open("icona.png", "wb") as f:
    f.write(response_img.content)

print("djęcie zostało zapisane")
