# 🧰 OS Module Basics – Python File & Directory Operations

This module provides a comprehensive overview of Python's built-in `os` and `os.path` modules. It's designed to help learners understand and practice essential operations like navigating directories, handling paths, managing files, and working with file metadata.

## 📁 Folder Structure
All examples are grouped by categories with clear comments and organized Python scripts.

---

## 🧭 Directory and File Management

| Function | Description |
|----------|-------------|
| `os.chdir(path)` | Change current working directory |
| `os.getcwd()` | Get current working directory |
| `os.listdir(path='.')` | List contents of a directory |
| `os.mkdir(path)` | Create a new directory |
| `os.rename(src, dst)` | Rename a file or folder |
| `os.remove(path)` | Remove a file |

---

## 📍 Path Handling (using `os.path`)

| Function | Description |
|----------|-------------|
| `os.path.exists(path)` | Check if a file or folder exists |
| `os.path.join(path, *paths)` | Join one or more path components |
| `os.path.abspath(path)` | Get absolute path |
| `os.path.dirname(path)` | Get directory name from a path |
| `os.path.basename(path)` | Get file/folder name from a path |
| `os.path.split(path)` | Split path into (head, tail) |
| `os.path.splitext(path)` | Split filename into (name, extension) |

---

## 📊 File Metadata

| Function | Description |
|----------|-------------|
| `os.path.getsize(path)` | Get file size in bytes |
| `os.path.getmtime(path)` | Last modification time |
| `os.path.getatime(path)` | Last access time |
| `os.path.getctime(path)` | Creation time (platform-dependent) |

---

## ✅ Type Checking

| Function | Description |
|----------|-------------|
| `os.path.isfile(path)` | Is the path a file? |
| `os.path.isdir(path)` | Is the path a directory? |
| `os.path.isabs(path)` | Is it an absolute path? |
| `os.path.islink(path)` | Is it a symbolic link? |
| `os.path.ismount(path)` | Is it a mount point? |

---

## 🛠️ Utility Functions

| Function | Description |
|----------|-------------|
| `os.path.relpath(path, start=os.curdir)` | Get relative path from a start point |
| `os.path.commonpath(paths)` | Get common path among multiple paths |
| `os.path.commonprefix(list)` | Get common prefix from path list |
| `os.path.expanduser(path)` | Expand `~` to user home directory |
| `os.path.expandvars(path)` | Expand environment variables |
| `os.path.normcase(path)` | Normalize case (Windows) |
| `os.path.normpath(path)` | Normalize path syntax |
| `os.path.splitdrive(path)` | Split drive from path (Windows only) |

---

## 🧠 Learning Purpose

This module is created to help you:

- Understand how Python interacts with the OS.
- Perform safe and effective file/directory manipulations.
- Practice path handling in a cross-platform manner.

Feel free to explore, modify, and expand upon the examples to enhance your Python scripting and automation skills!

---

## 📌 Author

**Urvil Patel**  
💻 Exploring Python Internals | 🛠️ Automating with Code | 📚 Always Learning  
