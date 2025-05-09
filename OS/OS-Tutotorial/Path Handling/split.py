import os

path = "folder/subfolder/file.txt"
print(os.path.split(path))  # Output: ('folder/subfolder', 'file.txt')


# os.path.split() – Split into (head, tail)