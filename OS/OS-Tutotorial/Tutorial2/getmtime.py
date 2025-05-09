import os
import time

mtime = os.path.getmtime("sample.txt")
print("Last Modified:", time.ctime(mtime))  # Human-readable format


# os.path.getmtime() – Get Last Modified Time