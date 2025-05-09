import os

# Create a file first (for demo)
with open("demo.txt", "w") as f:
    f.write("sample")

os.remove("demo.txt")  # Deletes the file


# Remove a File