import importlib
import os
from pathlib import Path

def docker_command(serverFolder,dataReceived):
    command = dataReceived[0].rstrip()
    if command == 'list':
        dockerModule = importlib.import_module("dockerManager")
        list = getattr(dockerModule, "list_container")
        return {'data':list()}
       # connection.sendall(f'{result}\r\n'.encode())
    if len(dataReceived) > 1:
        if command == 'create':
            serverName = dataReceived[1].rstrip()
            version = ''
            forgeversion = ''
            type = ''
            enviroment = {"EULA": "TRUE", "ONLINE_MODE": "FALSE"}
            if len(dataReceived) > 2:
                port = dataReceived[2].rstrip()
                if len(dataReceived) > 3:
                    type = dataReceived[3].rstrip()
                    enviroment['TYPE'] = type.upper()

                if len(dataReceived) > 4:
                    version = dataReceived[4].rstrip()
                    enviroment['VERSION'] = version
                if len(dataReceived) > 5:
                    forgeversion = dataReceived[5].rstrip()
                    enviroment['FORGEVERSION'] = forgeversion
                print(enviroment)
                directoryName = os.path.join(serverFolder, serverName)
                Path(directoryName).mkdir(parents=True, exist_ok=True)
                dockerModule = importlib.import_module("dockerManager")
                create = getattr(dockerModule, "create_container")
                if create(directoryName,serverName,int(port),enviroment):
                    yml_editor_module = importlib.import_module("utils.yml_editor")
                    yml_editor = getattr(yml_editor_module, "add_server_bungee")
                    yml_editor(serverFolder, serverName, port)
                    return {'status':True,'data':f'{serverName} created successful'}
                else:
                    return {'status':False,'data':f'{serverName} create with error. Check server container manager'}
            else:
               return {'status':False,'data':f'{serverName} You need inform a port.'}
        elif command == 'restart':
            serverName = dataReceived[1].rstrip()
            dockerModule = importlib.import_module("dockerManager")
            restart = getattr(dockerModule, "restart_container")
            if restart(serverName):
                return {'status':True,'data':f'{serverName} restarted successful'}
            else:
                return {'status':False,'data':f'{serverName} restarted with error. Check server container manager'}

        elif command == 'stop':
            serverName = dataReceived[1].rstrip()
            dockerModule = importlib.import_module("dockerManager")
            stop = getattr(dockerModule, "stop_container")
            if stop(serverName):
                return {'status':True,'data':f'{serverName} successfully stopped'}
            else:
               return {'status':False,'data':f'{serverName} stopped with error. Check server container manager'}
        elif command == 'start':
            serverName = dataReceived[1].rstrip()
            dockerModule = importlib.import_module("dockerManager")
            start = getattr(dockerModule, "start_container")
            if start(serverName):
               return {'status':True,'data':f'{serverName} successfully started'}
            else:
                return  {'status':False,'data':f'{serverName} started with error. Check server container manager'}
        elif command == 'remove':
            serverName = dataReceived[1].rstrip()
            directoryName = os.path.join(serverFolder, serverName)
            dockerModule = importlib.import_module("dockerManager")
            remove = getattr(dockerModule, "remove_container")
            try:
                if remove(serverName):
                    return {'status':True,'data':f'{serverName} successfully remove'}
                else:
                    return {'status':False,'data':f'{serverName} removed with error. Check server container manager'}
                for root, dirs, files in os.walk(directoryName, topdown=False):
                    for name in files:
                        os.remove(os.path.join(root, name))
                    for name in dirs:
                        os.rmdir(os.path.join(root, name))
                os.rmdir(directoryName)
            except Exception as error:
                return {'status':False,'data':f'{serverName} '+ str(error)}
    else:
        return {'status':False,'data':'cant execute this command'}
