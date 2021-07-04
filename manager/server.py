from logging import exception
import socket, pickle
import os
import sys
import docker
import importlib

from _thread import *

dockerClient = docker.from_env()
ServerSocket = socket.socket()
serverFolder = '/home/robertocpaes/minecraft-server'
host = '0.0.0.0'
port = 5000
ThreadCount = 0
try:
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
            list = getattr(dockerModule, "listContainer")
            result = {'data':list()}
            connection.sendall(f'{result}\r\n'.encode())
        elif len(dataReceived) > 1:
            if command == 'create':
                serverName = dataReceived[1].rstrip()
                if len(dataReceived) > 2:
                    port = dataReceived[2].rstrip()
                    directoryName = os.path.join(serverFolder, serverName)
                    os.mkdir(directoryName)
                    dockerModule = importlib.import_module("dockerManager")
                    create = getattr(dockerModule, "createContainer")
                    if create(directoryName,serverName,int(port)):
                        response = {'status':True,'data':f'{serverName} created successful'}
                    else:
                        response = {'status':False,'data':f'{serverName} create with error. Check server container manager'}
                else:
                        response = {'status':False,'data':f'{serverName} You need inform a port.'}
            elif command == 'restart':
                serverName = dataReceived[1].rstrip()
                dockerModule = importlib.import_module("dockerManager")
                restart = getattr(dockerModule, "restartContainer")
                if restart(serverName):
                    response = {'status':True,'data':f'{serverName} restarted successful'}
                else:
                    response = {'status':False,'data':f'{serverName} restarted with error. Check server container manager'}
            elif command == 'stop':
                serverName = dataReceived[1].rstrip()
                dockerModule = importlib.import_module("dockerManager")
                stop = getattr(dockerModule, "stopContainer")
                if stop(serverName):
                   response = {'status':True,'data':f'{serverName} successfully stopped'}
                else:
                   response = {'status':False,'data':f'{serverName} stopped with error. Check server container manager'}
            elif command == 'start':
                serverName = dataReceived[1].rstrip()
                dockerModule = importlib.import_module("dockerManager")
                start = getattr(dockerModule, "startContainer")
                if start(serverName):
                    response = {'status':True,'data':f'{serverName} successfully started'}
                else:
                    response = {'status':False,'data':f'{serverName} started with error. Check server container manager'}
            elif command == 'remove':
                serverName = dataReceived[1].rstrip()
                directoryName = os.path.join(serverFolder, serverName)
                dockerModule = importlib.import_module("dockerManager")
                remove = getattr(dockerModule, "removeContainer")
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