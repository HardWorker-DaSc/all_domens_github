import requests

url = 'https://api.github.com/meta'

response = requests.get(url)
data = response.json()


def extract(data):
    value = []

    for v in data.values():
        if isinstance(v, dict):
            value.extend(extract(v))
        else:
            value.append(v)

    return value


flat = extract(data)

flat_list = []

for sub in flat:
    if isinstance(sub, list):
        for x in sub:
            flat_list.append(x)

with open('domains.txt', 'w', encoding='utf-8') as file:
    for item in flat:
        file.write(f"{item}\n")