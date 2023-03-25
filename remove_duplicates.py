# serval 2023-03-13 

import os
import hashlib
import sys

def getallfiles(dir):
    allfiles = []
    for currentpath, folders, files in os.walk(dir):
        for file in files:
            allfiles.append((os.path.join(currentpath, file)))
    return allfiles

def gethash(filename):
    h = hashlib.sha1()
    with open(filename,"rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()

def removeduplicates(dir='.'):
    uniquehashes = []
    allfiles = getallfiles(dir)
    for file in allfiles:
        hash = gethash(file)
        if hash in uniquehashes:
            os.unlink(file)
        else:
            uniquehashes.append(hash)
    n = len(allfiles) - len(uniquehashes)
    print("Removed", n, "duplicates")

def printinfo():
        print("remove_duplicates: removes duplicate files (determined by sha1) in a given directory and its subdirectories")
        print("usage: python3 remove_duplicates.py [dir, defaults to .]")
        print("warning: this program will remove files!")

match len(sys.argv):
    case 0:
        printinfo()
    case 1:
        removeduplicates()
    case 2:
        if sys.argv[1] == "-h" or "--help":
            printinfo()
        else:
            if os.path.exists(sys.argv[1]):
                removeduplicates(sys.argv[1])
            else:
                print("Could not find requested directory")
    case _:
        printinfo()