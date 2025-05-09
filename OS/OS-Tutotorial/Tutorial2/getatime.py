import os
import time

atime = os.path.getatime("sample.txt")
print("Last Accessed:", time.ctime(atime))


# os.path.getatime() – Get Last Accessed Time