# 🛣️ Python `os.path` – Path Handling Functions

## 📌 Common Path Functions

| Function | Description |
|----------|-------------|
| `os.path.exists(path)`         | Check if the given path exists (file or folder). |
| `os.path.join(path, *paths)`   | Join one or more path components intelligently. |
| `os.path.abspath(path)`        | Return the absolute version of the path. |
| `os.path.dirname(path)`        | Get the directory name from the path. |
| `os.path.basename(path)`       | Get the file or folder name from the path. |
| `os.path.split(path)`          | Split path into a tuple `(head, tail)`. |
| `os.path.splitext(path)`       | Split path into `(file_name, extension)`. |

## 📌 Example Usage

```python
import os

path = "data/example.txt"

# Check if path exists
print(os.path.exists(path))  # True or False

# Join paths
new_path = os.path.join("data", "folder", "file.txt")
print(new_path)  # data/folder/file.txt (OS dependent)

# Get absolute path
print(os.path.abspath(path))

# Get directory name
print(os.path.dirname(path))  # data

# Get base name
print(os.path.basename(path))  # example.txt

# Split path into directory and file
print(os.path.split(path))  # ('data', 'example.txt')

# Split file name and extension
print(os.path.splitext(path))  # ('data/example', '.txt')
