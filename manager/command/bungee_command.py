import importlib
import os
from pathlib import Path
from manager.model.command import Command
from manager.dockerManager import remove_bungee, setup_bungee
def bungee_command(serverFolder, registerCommand):

    def create_bungee(dataReceived):
        if setup_bungee(serverFolder):
            response = {'status':True,'data':f'BungeeCord created and installed successful'}
        else:
            response = {'status':False,'data':f'BungeeCord Trow  with error. Check server container manager'}
        return response

    def remove_bungee(dataReceived):
        if remove_bungee():
            response = {'status':True,'data':f'BungeeCord removed successful'}
        else:
            response = {'status':False,'data':f'BungeeCord Trow  with error. Check server container manager'}
        return response

    Command('create-bungee', 1, 0, create_bungee, registerCommand.addCommand)
    Command('remove-bungee', 1, 0, remove_bungee, registerCommand.addCommand)
