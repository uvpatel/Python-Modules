import requests

r = requests.get('https://api.github.com/events', auth=('user', 'pass'))
print(r.status_code)

print(r.headers['content-type'])
'application/json; charset=utf8'
print(r.encoding)
'utf-8'
print(r.text)
'{"type":"User"...'
print(r.json())

