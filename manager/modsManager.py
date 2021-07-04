from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
def downloadFileExtract(directoryfolder,zipurl):
    try:
        with urlopen(zipurl) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zfile:
                zfile.extractall(directoryfolder)
        return True
    except:
        return False
def addMods(directoryfolder,zipurl):
    try:
        with urlopen(zipurl) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zfile:
                zfile.extractall(directoryfolder)
        return True
    except:
        return False
def clearMods(directoryfolder,zipurl):
    try:
        with urlopen(zipurl) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zfile:
                zfile.extractall(directoryfolder)
        return True
    except:
        return False
#downloadFile("/home/robertocpaes/minecraft-server/teste","http://update.displaybuttons.com/testezip.zip")
#urlopen("/home/robertocpaes/minecraft-server/teste","https://www.python.org/ftp/python/3.8.5/python-3.8.5-macosx10.9.pkg")