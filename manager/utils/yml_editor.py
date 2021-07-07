import ruamel.yaml
import os
from pathlib import Path

def add_server_bungee(serverDirectory,servername,port,motd = 'Apenas um teste'):
    yaml = ruamel.yaml.YAML()
    config_bungee = os.path.join(serverDirectory, "config.yml")
    print(serverDirectory, servername)
    with open(config_bungee) as fp:
        data = yaml.load(fp)
        data['servers'].update({servername:{'motd':motd,'address':f'{servername}:{port}','restricted':False}})
        print(data['servers'])
    with open(config_bungee, 'w') as fp:
        yaml.dump(data, fp)
def remove_server_bungee(serverDirectory,servername):
    yaml = ruamel.yaml.YAML()
    config_bungee = os.path.join(serverDirectory, "config.yml")
    print(serverDirectory, servername)
    with open(config_bungee) as fp:
        data = yaml.load(fp)
        del data['servers'][servername]
        print(data['servers'])
    with open(config_bungee, 'w') as fp:
        yaml.dump(data, fp)