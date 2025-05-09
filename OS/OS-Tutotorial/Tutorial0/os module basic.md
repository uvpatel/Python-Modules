# 🗂️ Python `os` Module – Basic File and Directory Operations

## 📌 Basic Functions

| Function | Description |
|---------|-------------|
| `os.chdir(path)`        | Change the current working directory to `path`. |
| `os.getcwd()`           | Get the current working directory. |
| `os.listdir(path='.')`  | List files and folders in the specified directory (default is current directory). |
| `os.mkdir(path)`        | Create a new directory at the specified path. |
| `os.rename(src, dst)`   | Rename a file or folder from `src` to `dst`. |
| `os.remove(path)`       | Remove (delete) the file at the specified path. |

## 📌 Example Usage

```python
import os

# Change to 'data' directory
os.chdir("data")

# Get current directory
print(os.getcwd())

# List contents of the current directory
print(os.listdir())

# Create a new folder named 'new_folder'
os.mkdir("new_folder")

# Rename folder from 'new_folder' to 'renamed_folder'
os.rename("new_folder", "renamed_folder")

# Remove a file named 'old_file.txt'
os.remove("old_file.txt")
