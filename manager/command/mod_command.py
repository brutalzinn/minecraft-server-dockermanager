import importlib
import os
def mod_command(serverFolder,dataReceived):
    command = dataReceived[0].rstrip()
    if command == 'addmod':
        serverName = dataReceived[1].rstrip()
        if len(dataReceived) > 2:
            url = dataReceived[2].rstrip()
            modsModule = importlib.import_module("modsManager")
            addMod = getattr(modsModule, "add_mods")
            directoryName = os.path.join(serverFolder, serverName)
            addMod(directoryName,url)
        else:
            return {'status':False,'data':f'{serverName} You need inform a url.'}
    elif command == 'clearmod':
        serverName = dataReceived[1].rstrip()
        modsReceived = ''
        modsList = []
        if len(dataReceived) > 2:
            for idx, val in enumerate(dataReceived):
                if idx > 1:
                    modsReceived = f'{modsReceived} {val.rstrip()}'
            modlist = modsReceived[1:].split(',')
            for  val in modlist:
                modsList.append(f'{val.rstrip()}.jar'.lower())
            modsModule = importlib.import_module("modsManager")
            clearMods = getattr(modsModule, "clear_mods")
            directoryName = os.path.join(serverFolder, serverName)
            if clearMods(directoryName,modsList):
                return {'status':True,'data':f'{serverName} mods successfully deleted'}
            else:
                return {'status':False,'data':f'{serverName} error deleting the mods.'}
        else:
            return {'status':False,'data':f'{serverName} You need inform a mod list between spaces.'}
    elif command == 'clearallmods':
        serverName = dataReceived[1].rstrip()
        modsModule = importlib.import_module("modsManager")
        clearAllMods = getattr(modsModule, "clear_all_mods")
        directoryName = os.path.join(serverFolder, serverName)
        clearAllMods(directoryName)