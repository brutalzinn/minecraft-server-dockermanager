import docker

dockerClient = docker.from_env()
environment={"EULA":"TRUE","TYPE":"FORGE","VERSION":"1.16.5","FORGEVERSION":"36.1.32"}
def createContainer(path,servername,port):
    container = dockerClient.containers.run(image="itzg/minecraft-server", name=servername,ports={'25565/tcp': port},
    environment=environment,volumes={path:{'bind':'/data','mode': 'rw'}},
    detach=True)
    return f'{container.short_id} Container created successful'
def removeContainer(servername):
    dockerClient.api.stop(servername)
    dockerClient.api.remove_container(servername)
