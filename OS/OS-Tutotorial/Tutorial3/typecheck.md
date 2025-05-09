# ✅ Python `os.path` – Type Checking Functions

## 📌 Type Checks

| Function | Description |
|----------|-------------|
| `os.path.isfile(path)`   | Checks if the path is a **regular file**. |
| `os.path.isdir(path)`    | Checks if the path is a **directory**. |
| `os.path.isabs(path)`    | Checks if the path is **absolute**. |
| `os.path.islink(path)`   | Checks if the path is a **symbolic link**. |
| `os.path.ismount(path)`  | Checks if the path is a **mount point** (e.g., root of a drive). |

## 📌 Example Usage

```python
import os

path = "data/example.txt"
dir_path = "data"
abs_path = os.path.abspath(path)

# Check if it's a file
print("Is file?", os.path.isfile(path))  # True or False

# Check if it's a directory
print("Is directory?", os.path.isdir(dir_path))  # True or False

# Check if path is absolute
print("Is absolute path?", os.path.isabs(abs_path))  # True

# Check if it's a symbolic link (if one exists)
print("Is symbolic link?", os.path.islink(path))  # Usually False

# Check if it's a mount point (e.g., 'C:\\' in Windows or '/' in Unix)
print("Is mount point?", os.path.ismount("/"))  # True on Unix-like systems
