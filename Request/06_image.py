import requests
from PIL import Image
from io import BytesIO

url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

print("Status Code:", r.status_code)
print("Content-Type:", r.headers.get('Content-Type'))

if r.status_code == 200 and 'image' in r.headers.get('Content-Type', ''):
    i = Image.open(BytesIO(r.content))
    i.show()
    fp = open("python_logo.png", "wb")
    i.save(fp, format="PNG")
    fp.write(r.content)
    fp.close()

    i.save("python_logo.png")
else:
    print("Failed to retrieve a valid image.")

