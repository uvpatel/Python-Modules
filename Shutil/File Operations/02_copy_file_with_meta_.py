'''
2. shutil.copy2(src, dst)
Same as copy(), but preserves metadata (timestamps, permissions).'''


import shutil

shutil.copy2("example.txt", "backup/example_copy2.txt")
