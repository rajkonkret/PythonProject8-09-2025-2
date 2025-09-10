from email.contentmanager import raw_data_manager

import chardet

# pip install chardet
with open('test.log', "r", encoding="utf-8") as f:
    raw_ata = f.read()
print(raw_ata)
# Nowe dane
# Dopisane
# Dopisane
# Dopśisane

# musimy wczytać binarnie - wymaganie chardet
with open("test.log", "rb") as f:
    raw_data = f.read()
print(raw_data)
# b'Nowe dane\r\nDopisane\r\nDopisane\r\nDop\xc5\x9bisane\r\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'MacRoman', 'confidence': 0.5922641509433962, 'language': ''}
# po zwiększeniu próbki wykrył prawidłowo
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}
encoding = result['encoding']
print("Kodoanie:", encoding)  # Kodoanie: utf-8

print(raw_data.decode(encoding=encoding))
# Kodoanie: utf-8
# Nowe dane
# Dopisane
# Dopisane
# Dopśąźćisane
