from logging import exception
import socket, pickle
import os
import sys
import docker
import importlib
from pathlib import Path
import ruamel.yaml
import sys

from _thread import *

dockerClient = docker.from_env()
ServerSocket = socket.socket()
serverFolder = '/home/robertocpaes/minecraft-server'
host = '0.0.0.0'
port = 5000
ThreadCount = 0
configFile = os.path.join(sys.path[0], "config.yml")

try:
    yaml = ruamel.yaml.YAML()
    if not os.path.exists(configFile):
        with open(configFile, 'w') as fp:
            data = {}
            data['run'] = 1
            yaml.dump(data, fp)
    with open(configFile) as fp:
        data = yaml.load(fp)
    if data['run'] == 0:
        data['run'] = 1
    with open(configFile, 'w') as fp:
        yaml.dump(data, fp)
    dockerModule = importlib.import_module("dockerManager")
    setup = getattr(dockerModule, "setup_docker")
    setup()
    ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ServerSocket.bind((host, port))

except socket.error as e:
    print(str(e))

print('Esperando conexão do mod..')
ServerSocket.listen(5)


def threaded_client(connection,address):
   # connection.send(str.encode('1'))
    while True:
        data = connection.recv(1024).decode()
        dataReceived = data.split(' ')
        command = dataReceived[0].rstrip()
        response = {}
        if command == 'test':
            connection.sendall('Esse é um teste de comunicação \r\n'.encode())
            print('teste recebido.')
        elif command == 'list':
            dockerModule = importlib.import_module("dockerManager")
            list = getattr(dockerModule, "list_container")
            result = {'data':list()}
            connection.sendall(f'{result}\r\n'.encode())
        elif len(dataReceived) > 1:
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
                        response = {'status':True,'data':f'{serverName} created successful'}
                    else:
                        response = {'status':False,'data':f'{serverName} create with error. Check server container manager'}
                else:
                        response = {'status':False,'data':f'{serverName} You need inform a port.'}
            elif command == 'restart':
                serverName = dataReceived[1].rstrip()
                dockerModule = importlib.import_module("dockerManager")
                restart = getattr(dockerModule, "restart_container")
                if restart(serverName):
                    response = {'status':True,'data':f'{serverName} restarted successful'}
                else:
                    response = {'status':False,'data':f'{serverName} restarted with error. Check server container manager'}
            elif command == 'addmod':
                #addmod #servername #url
                serverName = dataReceived[1].rstrip()
                if len(dataReceived) > 2:
                    url = dataReceived[2].rstrip()
                    modsModule = importlib.import_module("modsManager")
                    addMod = getattr(modsModule, "add_mods")
                    directoryName = os.path.join(serverFolder, serverName)
                    addMod(directoryName,url)
                else:
                    response = {'status':False,'data':f'{serverName} You need inform a url.'}
            elif command == 'clearallmods':
                serverName = dataReceived[1].rstrip()
                modsModule = importlib.import_module("modsManager")
                clearAllMods = getattr(modsModule, "clear_all_mods")
                directoryName = os.path.join(serverFolder, serverName)
                clearAllMods(directoryName)
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
                        response = {'status':True,'data':f'{serverName} mods successfully deleted'}
                    else:
                        response = {'status':False,'data':f'{serverName} error deleting the mods.'}
                else:
                    response = {'status':False,'data':f'{serverName} You need inform a mod list between spaces.'}
            elif command == 'stop':
                serverName = dataReceived[1].rstrip()
                dockerModule = importlib.import_module("dockerManager")
                stop = getattr(dockerModule, "stop_container")
                if stop(serverName):
                   response = {'status':True,'data':f'{serverName} successfully stopped'}
                else:
                   response = {'status':False,'data':f'{serverName} stopped with error. Check server container manager'}
            elif command == 'start':
                serverName = dataReceived[1].rstrip()
                dockerModule = importlib.import_module("dockerManager")
                start = getattr(dockerModule, "start_container")
                if start(serverName):
                    response = {'status':True,'data':f'{serverName} successfully started'}
                else:
                    response = {'status':False,'data':f'{serverName} started with error. Check server container manager'}
            elif command == 'remove':
                serverName = dataReceived[1].rstrip()
                directoryName = os.path.join(serverFolder, serverName)
                dockerModule = importlib.import_module("dockerManager")
                remove = getattr(dockerModule, "remove_container")
                try:
                    if remove(serverName):
                        response = {'status':True,'data':f'{serverName} successfully remove'}
                    else:
                        response = {'status':False,'data':f'{serverName} removed with error. Check server container manager'}
                    for root, dirs, files in os.walk(directoryName, topdown=False):
                        for name in files:
                            os.remove(os.path.join(root, name))
                        for name in dirs:
                            os.rmdir(os.path.join(root, name))
                    os.rmdir(directoryName)
                except Exception as error:
                    response = {'status':False,'data':f'{serverName} '+ str(error)}

            connection.sendall(f'{response}\r\n'.encode())
        else:
            error = {'status':False,'data':'cant execute this command'}
            connection.sendall(f'{error}\r\n'.encode())
        if not data:
            print("Desconectado. " + address[0])
            break
       # connection.sendall(str.encode(reply))
    connection.close()
while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client,address))
    #ThreadCount += 1
    #print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()