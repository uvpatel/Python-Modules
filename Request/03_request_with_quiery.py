import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)

#  we can acces f string useing url

# r = requests.get(f'https://httpbin.org/get?key1=value1&key2=value2')


print(r.json()) 



print(type(r.json())) # class 'dict'
# https://httpsbin.org/get?key1=value1&key2=value2