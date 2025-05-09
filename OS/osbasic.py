import os

os.chdir("data") # this changes the current working directory to "data"
print(os.getcwd()) # this prints the current working directory

folders = os.listdir("data") # this lists the files and folders in the current directory
print(folders) # this prints the list of files and folders in the current directory



for i in range(3):
    os.mkdir(f"Day{i}")


os.rename(f"Day{i}",f"Tutorials {i+1}") # this renames the folder "Day0" to "Tutorials 1"

os.remove(f"Day{i}") # this removes the folder "Day0" 