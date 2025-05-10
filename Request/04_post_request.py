import requests

r = requests.post('https://httpbin.org/post?', data = {'key1': 'value1', 'key2': 'value2'})

print(r.text)

# https://httpbin.org/post?a=b

