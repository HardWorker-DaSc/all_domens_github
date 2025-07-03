import requests

cloudflare = 'https://api.cloudflare.com/client/v4/ips?networks=jdcloud'
github = 'https://api.github.com/meta'

response_gh = requests.get(github)
response_cf = requests.get(cloudflare)

data_gh = response_gh.json()
data_cf = response_cf.json()


def extract(data):
    value = []

    for v in data.values():
        if isinstance(v, dict):
            value.extend(extract(v))
        else:
            value.append(v)

    return value


flat_gh = extract(data_gh)
flat_cf = extract(data_cf)

flat_list_cf = []
flat_list_gh = []

for sub in flat_gh:
    if isinstance(sub, list):
        for x in sub:
            flat_list_gh.append(x)

for sub in flat_cf:
    if isinstance(sub, list):
        for x in sub:
            flat_list_cf.append(x)

with open('domains_gh.txt', 'w', encoding='utf-8') as file:
    for item in flat_list_gh:
        file.write(f"{item}\n")

with open('domains_cf.txt', 'w', encoding='utf-8') as file:
    for item in flat_list_cf:
        file.write(f"{item}\n")