# 🛠️ Python `os.path` – Useful Utility Functions

## 📌 Path Utilities

| Function | Description |
|----------|-------------|
| `os.path.relpath(path, start=os.curdir)` | Returns the **relative path** from `start` to `path`. |
| `os.path.commonpath(paths)`              | Returns the **common path** among a list of paths. |
| `os.path.commonprefix(list)`             | Returns the **common string prefix** among a list (can break on path boundaries). |
| `os.path.expanduser(path)`               | Expands `~` to the current user’s home directory. |
| `os.path.expandvars(path)`               | Expands **environment variables** like `$HOME` or `%USERPROFILE%`. |
| `os.path.normcase(path)`                 | Normalizes the case of a path (Windows only: lowercases, Unix: no change). |
| `os.path.normpath(path)`                 | Normalizes path (removes `..`, extra slashes, etc.). |
| `os.path.splitdrive(path)`               | Splits drive and path (only useful in Windows). |

## 📌 Example Usage

```python
import os

path = "/home/urvil/projects/../notes.txt"
win_path = "C:\\Users\\Urvil\\Documents\\file.txt"
env_path = "$HOME/Desktop"
user_path = "~/Downloads"

# Relative path from current directory
print("Relative path:", os.path.relpath(path))

# Common path from list
print("Common path:", os.path.commonpath(["/home/urvil/docs", "/home/urvil/photos"]))

# Common prefix (not always path-safe)
print("Common prefix:", os.path.commonprefix(["/home/user1", "/home/user2"]))

# Expand user directory
print("Expanded user:", os.path.expanduser(user_path))

# Expand environment variable
print("Expanded vars:", os.path.expandvars(env_path))

# Normalize case (Windows)
print("Normalized case:", os.path.normcase(win_path))

# Normalize path
print("Normalized path:", os.path.normpath(path))

# Split drive (Windows only)
print("Split drive:", os.path.splitdrive(win_path))
