import os

def createDir(path):
    if not ((os.path.isdir(path))):
        os.mkdir(path)
    