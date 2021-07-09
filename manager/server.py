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
from model.command import Command
from model.register_command import RegisterCommand
from model.command_handler import CommandHandler
dockerClient = docker.from_env()
ServerSocket = socket.socket()
serverFolder = '/home/robertocpaes/minecraft-server'
host = '0.0.0.0'
port = 5000
ThreadCount = 0
configFile = os.path.join(sys.path[0], "config.yml")
# mod_command_module = importlib.import_module("mod_command")
# mod_command = getattr(mod_command_module, "modCommand")
docker_command_module = importlib.import_module("command.docker_command")
docker_command = getattr(docker_command_module, "docker_command")
registerCommand = RegisterCommand()
commandHandler = CommandHandler()
dockerModule = importlib.import_module("dockerManager")
docker_command(serverFolder, registerCommand)

try:
    yaml = ruamel.yaml.YAML()
    if not os.path.exists(configFile):
        with open(configFile, 'w') as fp:
            data = {}
            data['run'] = 0
            yaml.dump(data, fp)
    with open(configFile) as fp:
        data = yaml.load(fp)
        if data['run'] == 0:
            dockerModule = importlib.import_module("dockerManager")
            setup = getattr(dockerModule, "setup_docker")
            setup()
    with open(configFile) as fp:
        data = yaml.load(fp)
    if data['run'] == 0:
        data['run'] = 1
    with open(configFile, 'w') as fp:
        yaml.dump(data, fp)
    ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ServerSocket.bind((host, port))

except socket.error as e:
    print(str(e))

print('Esperando conexão do mod..')
ServerSocket.listen(5)

def teste():
    print('testando..')
    return True

Command('create-bungee', 1, 0, getattr(dockerModule, "setup_bungee"), registerCommand.addCommand)
Command('remove-bungee', 1, 0, getattr(dockerModule, "remove_bungee"), registerCommand.addCommand)
Command('teste', 1, 0, teste, registerCommand.addCommand)
def threaded_client(connection,address):
    while True:
        data = connection.recv(1024).decode()
        dataReceived = data.split(' ')
        command = dataReceived[0].rstrip()
        response = {}

        # if command == 'create-bungee':
        #     dockerModule = importlib.import_module("dockerManager")
        #     bungee = getattr(dockerModule, "setup_bungee")
        #     if bungee(serverFolder):
        #         response = {'status':True,'data':f'BungeeCord created and installed successful'}
        #     else:
        #         response = {'status':False,'data':f'BungeeCord Trow  with error. Check server container manager'}
        #     connection.sendall(f'{response}\r\n'.encode())
        # elif command == 'remove-bungee':
        #     dockerModule = importlib.import_module("dockerManager")
        #     bungee = getattr(dockerModule, "remove_bungee")
        #     if bungee():
        #         response = {'status':True,'data':f'BungeeCord removed successful'}
        #     else:
        #         response = {'status':False,'data':f'BungeeCord Trow  with error. Check server container manager'}
        #     connection.sendall(f'{response}\r\n'.encode())
        result = commandHandler.checkCommand(dataReceived, registerCommand.getCommands)
        connection.sendall(f'{result}\r\n'.encode())
        #result = docker_command(serverFolder, dataReceived)
        #connection.sendall(f'{result}\r\n'.encode())
        if not data:
            print("Desconectado. " + address[0])
            break
    connection.close()
while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, address))
ServerSocket.close()