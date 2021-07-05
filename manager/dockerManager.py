import docker

dockerClient = docker.from_env()
# environment = {"EULA": "TRUE", "TYPE": "FORGE", "VERSION": "1.16.5", "FORGEVERSION": "36.1.32", "ONLINE_MODE": "FALSE"}


def create_container(path, servername, port,environment):
    try:
        dockerClient.containers.run(image="itzg/minecraft-server:java8", name=servername, ports={'25565/tcp': port},
                                    network='bungee',
                                     environment=environment, volumes={path: {'bind': '/data', 'mode': 'rw'}},
                                    detach=True)
        return True
    except Exception as err:
        print(err)
        return False
def setup_docker():
    dockerClient.images.pull("itzg/minecraft-server")
def setup_bungee(serverdirectory):
    try:
        dockerClient.networks.create("bungee")
        dockerClient.images.pull("itzg/bungeecord")
        environment = {"TYPE":"WATERFALL"}
        dockerClient.containers.run(image="itzg/bungeecord", name='bungeecord', ports={'25577/tcp': 25577},
        network='bungee',
        environment=environment,
        volumes={serverdirectory: {'bind': '/server', 'mode': 'rw'}},
        detach=True)
        return True
    except Exception as err:
        print(err)
        return False
def remove_bungee():
    try:
        dockerClient.api.stop('bungeecord')
        dockerClient.api.remove_container('bungeecord')
        dockerClient.images.remove("itzg/bungeecord")
        dockerClient
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
    containerList = dockerClient.containers.list(all=True, filters={"ancestor": ["itzg/minecraft-server:java8"]})
    for item in containerList:
        containerInfo = dockerClient.containers.get(item.id)
        ports = containerInfo.attrs['HostConfig']['PortBindings'].items()
        finalPort = 0
        for key, value in ports:
            finalPort = value[0]['HostPort']
        list.append({'name': item.name, 'status': item.status, 'port': f"{finalPort}"})
    return list
