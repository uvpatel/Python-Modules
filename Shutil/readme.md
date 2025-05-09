# 🧰 `shutil` Module Basics – High-Level File & Directory Operations in Python

This module showcases the power of Python’s built-in `shutil` module, providing high-level utilities for automating file and directory operations such as copying, moving, deleting, and archiving.

Ideal for scripting, backups, deployment automation, and file management tasks.

---
## 📁 Folder Structure

All examples are neatly organized into standalone scripts with clear usage of each function. This helps in focused learning and quick reference.

---
## 📄 File Operations

| Function | Description |
|----------|-------------|
| shutil.copy(src, dst) | Copy a file to another file or directory (metadata not preserved) |
| shutil.copy2(src, dst) | Same as copy(), but preserves metadata like timestamps |
| shutil.copyfile(src, dst) | Copy file contents (src and dst must both be files) |
| shutil.move(src, dst) | Move a file or directory to a new location |

---

## 📂 Directory Operations

| Function | Description |
|----------|-------------|
| shutil.copytree(src, dst, dirs_exist_ok=False) | Recursively copy an entire directory tree |
| shutil.rmtree(path) | Recursively delete a directory and its contents |

---

## 📦 Archiving & Extraction

| Function | Description |
|----------|-------------|
| shutil.make_archive(base_name, format, root_dir) | Create an archive (e.g., ZIP or TAR) from a directory |
| shutil.unpack_archive(filename, extract_dir) | Unpack an archive into a specified directory |

---

## 🧪 Utility Functions

| Function | Description |
|----------|-------------|
| shutil.which(cmd) | Find the path of a command in the system PATH |
| shutil.disk_usage(path) | Return total, used, and free disk space at the given path |

---

> 🔧 Output folders and archives (e.g., `archive/`, `backup/`, `project_backup.zip`) are created dynamically by the scripts.

---

## 📄 File Operations

These scripts demonstrate essential file manipulation tasks using `shutil`.

| Function                      | Description                                                     |
|-------------------------------|-----------------------------------------------------------------|
| `shutil.copy(src, dst)`       | Copies file content to a destination (without metadata)         |
| `shutil.copy2(src, dst)`      | Same as `copy()`, but also preserves file metadata              |
| `shutil.copyfile(src, dst)`   | Copies content from source to destination (both must be files)  |
| `shutil.move(src, dst)`       | Moves or renames a file or directory                            |

---

## 📂 Directory Operations

Perform recursive actions on folders and directory trees.

| Function                                         | Description                                                  |
|--------------------------------------------------|--------------------------------------------------------------|
| `shutil.copytree(src, dst, dirs_exist_ok=False)` | Recursively copies a directory tree                          |
| `shutil.rmtree(path)`                            | Recursively deletes a directory and all its contents         |

---

## 📦 Archiving & Extraction

Easily compress or extract directories with just one line of code.

| Function                                          | Description                                            |
|---------------------------------------------------|--------------------------------------------------------|
| `shutil.make_archive(base_name, format, root_dir)`| Creates an archive (ZIP, TAR, etc.) from a directory  |
| `shutil.unpack_archive(filename, extract_dir)`     | Extracts an archive into the specified directory       |

---

## 🧪 Utility Functions

Helpful one-liners for working with system resources and command-line tools.

| Function                  | Description                                                       |
|---------------------------|-------------------------------------------------------------------|
| `shutil.which(cmd)`       | Returns the path of a command if found in the system PATH         |
| `shutil.disk_usage(path)` | Returns total, used, and free disk space for the given location   |

---

## 🎯 Learning Outcomes

By exploring these examples, you'll:

- 📁 Automate file and directory operations with ease  
- 🗃️ Perform advanced copying with full metadata support  
- 🧰 Create and extract compressed archives programmatically  
- ⚙️ Analyze disk usage and locate system-level tools  
- 🧠 Improve scripting skills and understand real-world automation use cases  

---

## 🧠 Why Learn `shutil`?

The `shutil` module is perfect for:

- Backup scripts and deployment pipelines  
- Cleaning up temporary directories or logs  
- Automating repetitive file system tasks  
- Creating cross-platform Python automation scripts  

---

## ⚙️ Python Compatibility

- ✅ **Python 3.8+ recommended** (for full `copytree()` support with `dirs_exist_ok`)
- ❌ No external dependencies required

---

## 👨‍💻 Author

**Urvil Patel**  
🛠 Python Automation Explorer | 📂 System Scripts Enthusiast | 🚀 Lifelong Learner

---

## 🧾 License

This project is released under the **MIT License** — free for personal and commercial use.

---

## 🤝 Contributions

Have suggestions or improvements?  
Feel free to fork this repository, submit a PR, or open an issue!

---

