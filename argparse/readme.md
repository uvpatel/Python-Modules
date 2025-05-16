
# 🧰 Command Line Utilities in Python (`argparse`)

Command line utilities are programs that run from the terminal or command prompt. Python’s built-in `argparse` module helps create these utilities easily, allowing us to define arguments that users can pass during script execution.

---

## 📌 Why Use `argparse`?

- Accept arguments from users.
- Create flexible command-line tools.
- Improve usability by auto-generating help messages (`-h`).
- Set default values and input types.

---

## 🧠 Basic Syntax

```python
import argparse

parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("arg1", help="description of argument 1")
parser.add_argument("arg2", help="description of argument 2")

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.arg1)
print(args.arg2)
```

---

## 🧪 Examples

### 1️⃣ Adding Optional Arguments

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--optional", help="description of optional argument", default="default_value")
args = parser.parse_args()

print(args.optional)
```

Usage:

```bash
python script.py -o Hello
# OR
python script.py --optional Hello
```

---

### 2️⃣ Adding Positional Arguments

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("positional", help="description of positional argument")
args = parser.parse_args()

print(args.positional)
```

Usage:

```bash
python script.py Hello
```

---

### 3️⃣ Adding Arguments with Type

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="description of integer argument")
args = parser.parse_args()

print(args.n)
```

Usage:

```bash
python script.py -n 5
```

---

### 4️⃣ Real Use Case: File Downloader

```python
import argparse
import requests

def download_file(url, local_filename=None): 
    if local_filename is None:
        local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

parser = argparse.ArgumentParser()
parser.add_argument("url", help="URL of the file to download")
parser.add_argument("-o", "--output", type=str, help="Name to save the file as", default=None)
args = parser.parse_args()

print("Downloading from:", args.url)
print("Saving as:", args.output or "Default filename from URL")
download_file(args.url, args.output)
```

Usage:

```bash
python main.py "https://imagej.net/images/Cell_Colony.jpg" -o Cell_Colony.jpg
```

---

## 🎯 Conclusion

Creating command-line tools using `argparse` helps make your Python scripts more interactive and reusable. Whether you're building small utilities or full-scale apps, mastering `argparse` is a valuable skill for any developer.

---