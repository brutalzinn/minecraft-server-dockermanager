import importlib
import os
from pathlib import Path
from manager.model.command import Command

def docker_command(serverFolder, registerCommand):
    dockerModule = importlib.import_module("dockerManager")
    Command('list', 1, 0, getattr(dockerModule, "list_container"), registerCommand.addCommand)
    def create_command(dataReceived):
            serverName = dataReceived[1].rstrip()
            version = ''
            forgeversion = ''
            type = ''
            if len(dataReceived) > 2:
                port = dataReceived[2].rstrip()
                enviroment = {"EULA": "TRUE", "ONLINE_MODE": "FALSE", "SERVER_PORT": port}

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
    def restart(dataReceived):
            serverName = dataReceived[1].rstrip()
            dockerModule = importlib.import_module("dockerManager")
            restart = getattr(dockerModule, "restart_container")
            if restart(serverName):
                return {'status':True,'data':f'{serverName} restarted successful'}
            else:
                return {'status':False,'data':f'{serverName} restarted with error. Check server container manager'}

    def stop(dataReceived):
            serverName = dataReceived[1].rstrip()
            dockerModule = importlib.import_module("dockerManager")
            stop = getattr(dockerModule, "stop_container")
            if stop(serverName):
                return {'status':True,'data':f'{serverName} successfully stopped'}
            else:
               return {'status':False,'data':f'{serverName} stopped with error. Check server container manager'}
    def start(dataReceived):
            serverName = dataReceived[1].rstrip()
            dockerModule = importlib.import_module("dockerManager")
            start = getattr(dockerModule, "start_container")
            if start(serverName):
               return {'status':True,'data':f'{serverName} successfully started'}
            else:
                return  {'status':False,'data':f'{serverName} started with error. Check server container manager'}
    def remove(dataReceived):
            serverName = dataReceived[1].rstrip()
            directoryName = os.path.join(serverFolder, serverName)
            dockerModule = importlib.import_module("dockerManager")
            remove = getattr(dockerModule, "remove_container")
            try:
                if remove(serverName):
                    for root, dirs, files in os.walk(directoryName, topdown=False):
                        for name in files:
                            os.remove(os.path.join(root, name))
                        for name in dirs:
                            os.rmdir(os.path.join(root, name))
                    os.rmdir(directoryName)
                    yml_editor_module = importlib.import_module("utils.yml_editor")
                    yml_editor = getattr(yml_editor_module, "remove_server_bungee")
                    yml_editor(serverFolder, serverName)
                    return {'status':True,'data':f'{serverName} successfully remove'}
                else:
                    return {'status':False,'data':f'{serverName} removed with error. Check server container manager'}
            except Exception as error:
                return {'status':False,'data':f'{serverName} '+ str(error)}

    Command('create', 6, 4, create_command, registerCommand.addCommand)
    Command('stop', 1, 1, stop, registerCommand.addCommand)
    Command('restart', 1, 1, restart, registerCommand.addCommand)
    Command('start', 1, 1, start, registerCommand.addCommand)
    Command('remove', 1, 1, remove, registerCommand.addCommand)