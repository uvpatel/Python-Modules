import os
import time

ctime = os.path.getctime("sample.txt")
print("Created On:", time.ctime(ctime))


#  os.path.getctime() – Get Creation Time