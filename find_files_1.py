import os
import fnmatch

for filename in os.listdir("/PATH"):
    if fnmatch.fnmatch(filename, "*Pandas*.*"):
        print(filename)

    if fnmatch.fnmatch(filename, "*Django*.*"):
        print(filename)

    if fnmatch.fnmatch(filename, "*Flask*.*"):
        print(filename)

