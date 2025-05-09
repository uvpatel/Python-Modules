import shutil

'''
7. shutil.disk_usage(path)
Returns disk usage statistics about the given path: (total, used, free) in bytes.'''

usage = shutil.disk_usage("/")
print(f"Total: {usage.total}, Used: {usage.used}, Free: {usage.free}")
