import os
import time
import math

class FileNode():
    def __init__(self, name : str, path : str, attribs : dict):
        self.name = name
        self.path = path
        self.attribs = attribs
        

class FileTree():
    def __init__(self, name):
        self.name = name
        self.directories = []
        self.files = []

    def addFile(self, file : FileNode):
        self.files.append(file)

    def addDir(self, directory):
        self.directories.append(directory)

    def searchDir(self, name :str):
        for dire in self.directories:
            if dire.name == name:
                return dire

        return None

    def searchFile(self, name : str):
        for file in self.files:
            if file.name == name:
                return file
        return None


    @staticmethod
    def createFromPath(path : str):
        try:
            neim = os.path.basename(path)
            #   print(neim)
            tree = FileTree(neim)
            dirs, files = processPath(path)
            for direc in dirs:
                tree.addDir(FileTree.createFromPath(path + "\\" + direc))
            for file in files :
                absPath = path + "\\" + file
                atribs = getFileAttribs(absPath)
                tree.addFile(FileNode(file, absPath, atribs))
            return tree
        except:
            return None

def convert_size(size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

def formatDate(seconds):
    result = time.localtime(seconds)
    return time.strftime("%d/%m/%Y - %H:%M:%S", result)
            

def getFileAttribs(path : str):
    atts = dict()
    attibs = os.stat(path)
    atts['size'] = convert_size(attibs.st_size)
    atts['created'] = formatDate(attibs.st_ctime)
    atts['modificated'] = formatDate(attibs.st_mtime)
    return atts

def processPath(path : str):
    dirs = []
    files = []
    for file in os.listdir(path):
        if os.path.isdir(path + "\\" + file):
            dirs.append(file)
        else :
            files.append(file)

    return dirs, files
        
    
class Computer():

    def __init__(self, name : str, path : str):
        self.name = name
        self.path = path
        self.tree = FileTree.createFromPath(path)

class DirectoryManager():
    pass
    @staticmethod
    def createDir(name : str):
        pass


