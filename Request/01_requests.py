import requests


r = requests.get("https://www.github.com")
print(r.text)

with open("github.html", "w") as f:
    f.write(r.text)
    