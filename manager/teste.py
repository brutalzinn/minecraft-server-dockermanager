import socket
import os
import docker
from _thread import *

dockerClient = docker.from_env()
ServerSocket = socket.socket()
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
    connection.send(str.encode('1'))
    while True:
        data = connection.recv(1024).decode()
        dataReceived = data.split(' ')
        command = dataReceived[0].rstrip()
        image = dataReceived[1].rstrip()
        commandList = ''
        if command == 'run':
            if len(dataReceived) > 2:
                for item in enumerate(dataReceived):
                    if item[0] > 1:
                        commandList = commandList.join(f'{item[1].rstrip()} ')
                print(commandList.rstrip())
                dockerClient.containers.run(image,commandList)
            else:
                dockerClient.containers.run(image)
        if command == 'remove':
            dockerClient.containers.run(image)
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
#ServerSocket.close()