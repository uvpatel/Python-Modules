import os

print(os.path.isabs("folder/file.txt"))         # False
print(os.path.isabs("/Users/urvil/file.txt"))   # True (on Unix/Mac)


# os.path.isabs() – Is Absolute Path?