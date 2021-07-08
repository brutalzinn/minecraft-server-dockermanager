# import subprocess
# import socket
# HOST = '0.0.0.0'
# PORT = 5000
# sSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sSocket.bind((HOST,PORT))
# sSocket.listen()
# print("Aguardando conexão com o mod.")
# conn, ender = sSocket.accept()
# print("Conectando em", ender)
# while True:
#     data = conn.recv(1024)
#     if not data:
#         print("Fechando a conexão")
#         conn.close()
#         break
#     s = subprocess.getstatusoutput(data.decode())
#     conn.sendall(str(s).encode())
import importlib
# serverFolder = '/home/robertocpaes/minecraft-server'
# yml_editor_module = importlib.import_module("utils.yml_editor")
# yml_editor = getattr(yml_editor_module, "add_server_bungee")
# yml_editor(serverFolder, 'teste',25566)


from model.command import Command
from model.register_command import RegisterCommand
from model.command_handler import CommandHandler

def createTest():
    print('teste de função create.')
    return 'create suceffull'
def stopTest():
    print('teste de função stop.')
    return 'stop suceffull'

# commandTester = [['create', 'servername', '25565', 'forge', '1.16.5', '13.2.6'],['stop', 'containername']]
commandReceived = ['create', 'servername', '25565', 'forge', '1.16.5', '13.2.6'] #trying to simulate a command.
# commandReceived = ['stop', 'containername']
registerCommand = RegisterCommand()
commandum = Command('create', 6, 5, createTest, registerCommand.addCommand)
commanddois = Command('stop', 1, 0, stopTest, registerCommand.addCommand)
commandtres = Command('restart', 1, 0, False, registerCommand.addCommand)
commandHandler = CommandHandler()

# for item in commandTester:
response = commandHandler.checkCommand(commandReceived, registerCommand.getCommands)
print(response)
for obj in registerCommand.getCommands():
    print( obj.command, obj.max_arg, obj.min_arg, sep =' ' )
