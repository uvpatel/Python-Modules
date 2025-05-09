import os

path = "folder//subfolder/../file.txt"
print(os.path.normpath(path))  # Output: folder/file.txt


# 🔹 os.path.normpath() – Normalize Path