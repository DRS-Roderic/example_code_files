import shutil
import os
import fnmatch

file_source = "/media/pi/My Book/Books/Web and computer/"
file_destination = "/media/pi/My Book/Books/Web and computer/Other programing languages/"


for filename in os.listdir(file_source):

    if fnmatch.fnmatch(filename, "* Ethereum * .*"):
        print(filename)
        shutil.move(file_source + filename, file_destination)

    if fnmatch.fnmatch(filename, "* Typescript *.*"):
        print(filename)
        shutil.move(file_source + filename, file_destination)

    if fnmatch.fnmatch(filename, "* Ethereum *.*"):
        print(filename)
        shutil.move(file_source + filename, file_destination)

    
