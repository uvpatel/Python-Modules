# 📄 Python `os.path` – File Metadata Functions

## 📌 File Metadata

| Function | Description |
|----------|-------------|
| `os.path.getsize(path)`   | Returns the size of the file in bytes. |
| `os.path.getmtime(path)`  | Returns the last modified time (timestamp). |
| `os.path.getatime(path)`  | Returns the last accessed time (timestamp). |
| `os.path.getctime(path)`  | Returns the creation time (timestamp, platform-dependent). |

> 🕒 These time values are in **seconds since epoch**. Use `time.ctime()` or `datetime` module to convert them into readable format.

## 📌 Example Usage

```python
import os
import time

path = "data/example.txt"

# File size in bytes
print("Size:", os.path.getsize(path), "bytes")

# Last modified time
print("Modified:", time.ctime(os.path.getmtime(path)))

# Last accessed time
print("Accessed:", time.ctime(os.path.getatime(path)))

# Creation time
print("Created:", time.ctime(os.path.getctime(path)))
