# Import Module
import os
from datetime import datetime

# Folder Path
path = './data'

# Change the directory
os.chdir(path)


def changeFilesName():

    for count, filename in enumerate(os.listdir()):

        aux = os.path.getmtime(filename)
        hola = datetime.fromtimestamp(aux).strftime('%Y-%m-%d %H-%M-%S')
        extension = os.path.splitext(filename)[1]

        src = filename
        dst = hola + extension

        os.rename(src, dst)


def detectDirectories():

    for count, filename in enumerate(os.listdir()):
        if os.path.isdir(filename):
            print(filename + ' is a directory!')
        else:
            print(filename + ' is a file')

            aux = os.path.getmtime(filename)
            hola = datetime.fromtimestamp(aux).strftime('%Y-%m-%d %H-%M-%S')
            extension = os.path.splitext(filename)[1]

            src = filename
            dst = hola + extension

            os.rename(src, dst)


def main():
    detectDirectories()
    # changeFilesName()


main()
