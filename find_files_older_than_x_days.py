import os
import time
import datetime
import sys
path = sys.argv[1]#"/mnt/c/Users/silambarasankarthike/Downloads"
now = time.time()
#print(datetime.datetime.fromtimestamp(now - 7 * 86400).strftime('%c'))
X_days_older = now - int(sys.argv[2]) * 86400

count = 0
for f in os.listdir(path):
    if os.path.isfile(os.path.join(path, f)):
       if os.stat(os.path.join(path, f)).st_mtime < X_days_older:
           count += 1
           print(os.path.join(path, f))
           #os.remove(os.path.join(path, f))
print(count)

