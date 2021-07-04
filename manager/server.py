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


def threaded_client(connection):
   # connection.send(str.encode('1'))
    while True:
        data = connection.recv(1024).decode()
        dataReceived = data.split(' ')
        command = dataReceived[0].rstrip()
        if command == 'create':
            port = dataReceived[2].rstrip()
            serverName = dataReceived[1].rstrip()
            directoryName = os.path.join(serverFolder, serverName)
            os.mkdir(directoryName)
            dockerModule = importlib.import_module("dockerManager")
            ds = getattr(dockerModule, "createContainer")
            response = ds(directoryName,serverName,int(port))
            connection.sendall(str.encode(response))
        if command == 'test':
            connection.sendall('Esse é um teste de comunicação \r\n'.encode())
            print('teste recebido.')
        if command == 'list':
            dockerModule = importlib.import_module("dockerManager")
            list = getattr(dockerModule, "listContainer")
            result = {'data':list()}
            connection.sendall(f'{result} \r\n'.encode())
        if command == 'restart':
            serverName = dataReceived[1].rstrip()
            dockerModule = importlib.import_module("dockerManager")
            restart = getattr(dockerModule, "restartContainer")
            if restart(serverName):
                connection.sendall({'status':True,'data':f'{serverName} restarted successful \r\n'.encode()})
            else:
                connection.sendall({'status':False,'data':f'{serverName} restarted with error. Check server container manager \r\n'.encode()})
        if command == 'stop':
            serverName = dataReceived[1].rstrip()
            dockerModule = importlib.import_module("dockerManager")
            stop = getattr(dockerModule, "stopContainer")
            if  stop(serverName):
                connection.sendall({'status':True,'data':f'{serverName} successfully stopped \r\n'.encode()})
            else:
                connection.sendall({'status':False,'data':f'{serverName} stopped with error. Check server container manager \r\n'.encode()})
        if command == 'start':
            serverName = dataReceived[1].rstrip()
            dockerModule = importlib.import_module("dockerManager")
            start = getattr(dockerModule, "startContainer")
            if start(serverName):
                connection.sendall({'status':True,'data':f'{serverName} successfully started \r\n'.encode()})
            else:
                connection.sendall({'status':False,'data':f'{serverName} started with error. Check server container manager \r\n'.encode()})
        if command == 'remove':
            serverName = dataReceived[1].rstrip()
            directoryName = os.path.join(serverFolder, serverName)
            dockerModule = importlib.import_module("dockerManager")
            remove = getattr(dockerModule, "removeContainer")
            if remove(serverName):
                connection.sendall({'status':True,'data':f'{serverName} successfully remove \r\n'.encode()})
            else:
                connection.sendall({'status':True,'data':f'{serverName} removed with error. Check server container manager \r\n'.encode()})
                return False
            for root, dirs, files in os.walk(directoryName, topdown=False):
                for name in files:
                     os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(directoryName)
        if not data:
            break
       # connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()