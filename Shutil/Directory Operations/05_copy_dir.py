'''

5. shutil.copytree(src, dst, dirs_exist_ok=False)
Recursively copies an entire directory tree from src to dst.


Use dirs_exist_ok=True (Python 3.8+) if dst already exists.
'''

import shutil

shutil.copytree("my_folder", "backup_folder")
