import docker

dockerClient = docker.from_env()
# environment = {"EULA": "TRUE", "TYPE": "FORGE", "VERSION": "1.16.5", "FORGEVERSION": "36.1.32", "ONLINE_MODE": "FALSE"}


def create_container(path, servername, port,environment):
    try:
        dockerClient.containers.run(image="itzg/minecraft-server", name=servername, ports={'25565/tcp': port},
                                    environment=environment, volumes={path: {'bind': '/data', 'mode': 'rw'}},
                                    detach=True)
        return True
    except Exception as err:
        print(err)
        return False
def setup_docker():
    dockerClient.images.pull("itzg/minecraft-server")
    dockerClient.images.pull("itzg/bungeecord")
def setup_bungee(serverdirectory):
    try:
        dockerClient.containers.run(image="itzg/bungeecord", name='bungeecord', ports={'25565/tcp': 25565},
        volumes={serverdirectory: {'bind': '/data', 'mode': 'rw'}},
        detach=True)
        return True
    except:
        return False
def remove_container(servername):
    try:
        dockerClient.api.stop(servername)
        dockerClient.api.remove_container(servername)
        return True
    except:
        return False


def restart_container(servername):
    try:
        dockerClient.api.restart(servername)
        return True
    except:
        return False


def start_container(servername):
    try:
        dockerClient.api.start(servername)
        return True
    except:
        return False


def stop_container(servername):
    try:
        dockerClient.api.stop(servername)
        return True
    except:
        return False


def list_container():
    list = []
    containerList = dockerClient.containers.list(all=True, filters={"ancestor": ["itzg/minecraft-server"]})
    for item in containerList:
        containerInfo = dockerClient.containers.get(item.id)
        ports = containerInfo.attrs['HostConfig']['PortBindings'].items()
        finalPort = 0
        for key, value in ports:
            finalPort = value[0]['HostPort']
        list.append({'name': item.name, 'status': item.status, 'port': f"{finalPort}"})
    return list
