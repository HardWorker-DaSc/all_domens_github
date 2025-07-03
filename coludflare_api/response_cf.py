import requests

cloudflare = 'https://api.cloudflare.com/client/v4/ips?networks=jdcloud'

response = requests.get(cloudflare)

data = response.json()


def extract(data):
    value = []

    for v in data.values():
        if isinstance(v, dict):
            value.extend(extract(v))
        else:
            value.append(v)

    return value


flat_cf = extract(data)

flat_list_cf = []

for sub in flat_cf:
    if isinstance(sub, list):
        for x in sub:
            flat_list_cf.append(x)

with open('api_cloudflare.txt', 'w', encoding='utf-8') as file:
    for item in flat_list_cf:
        file.write(f"{item}\n")