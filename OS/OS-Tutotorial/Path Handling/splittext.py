import os

filename = "data.csv"
print(os.path.splitext(filename))  # Output: ('data', '.csv')


# os.path.splitext() – Split into (name, extension)