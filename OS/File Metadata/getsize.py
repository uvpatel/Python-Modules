import os

# Create a file to test
with open("sample.txt", "w") as f:
    f.write("Hello, world!")

print(os.path.getsize("sample.txt"))  # Output: 13


# os.path.getsize() – Get File Size (in bytes)