import os
import fnmatch

for filename in os.listdir("/media/pi/My Book/Books/Web and computer/Python, PyTorch, Kivy, PyQt, Apache Airflow"):
    if fnmatch.fnmatch(filename, "*Pandas*.*"):
        print(filename)

    if fnmatch.fnmatch(filename, "*Django*.*"):
        print(filename)

    if fnmatch.fnmatch(filename, "*Flask*.*"):
        print(filename)

