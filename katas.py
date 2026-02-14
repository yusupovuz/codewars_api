import requests
from pprint import pprint
name = input('Enter the name of the kata: ').lower().split()
name = '-'.join(name)
url = f'https://www.codewars.com/api/v1/code-challenges/{name}'
response = requests.get(url)
data = response.json()
if 'success' in data.keys():
    print('Invalid name of Kata')
else:
    desc = {}
    desc['name'] = data['name']
    desc['category'] = data['category']
    desc['languages'] = data['languages']
    desc['url'] = data['url']
    desc['rank'] = data['rank']['name']
    desc['description'] = data['description']
    desc['tags'] = data['tags']
    pprint(desc)