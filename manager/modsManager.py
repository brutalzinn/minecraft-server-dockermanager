from io import BytesIO
import os
from urllib.request import urlopen
from zipfile import ZipFile
from pathlib import Path
def downloadFileExtract(directoryfolder,zipurl):
    try:
        with urlopen(zipurl) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zfile:
                zfile.extractall(directoryfolder)
        return True
    except:
        #return False
        raise Exception()
def addMods(directoryfolder,url):
    try:
        modFolder = os.path.join(directoryfolder, "mods")
        Path(modFolder).mkdir(parents=True, exist_ok=True)
        downloadFileExtract(modFolder,url)
        return True
    except:
        return False
def clearAllMods(directoryfolder):
    try:
        modFolder = os.path.join(directoryfolder, "mods")
        for root, dirs, files in os.walk(directoryfolder, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        Path(modFolder).rmdir(parents=True, exist_ok=True)
        return True
    except:
        return False
def clearMods(directoryfolder,mods):
    try:
        modFolder = os.path.join(directoryfolder, "mods")
        print(modFolder)
        print(mods)
        modsTotal = len(mods)
        print("before",modsTotal)
        for root, dirs, files in os.walk(modFolder, topdown=False):
            for name in files:
                if name.lower() in mods:
                    os.remove(os.path.join(root, name))
                    modsTotal = modsTotal - 1
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        #Path(modFolder).rmdir(parents=True, exist_ok=True)
        if modsTotal == 0:
            return True
        else:
            return False
    except:
        return False
#downloadFile("/home/robertocpaes/minecraft-server/teste","http://update.displaybuttons.com/testezip.zip")
#urlopen("/home/robertocpaes/minecraft-server/teste","https://www.python.org/ftp/python/3.8.5/python-3.8.5-macosx10.9.pkg")
#addMods("/home/robertocpaes/minecraft-server/teste","http://update.displaybuttons.com/testezip.zip")
