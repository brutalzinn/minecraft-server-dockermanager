import docker

dockerClient = docker.from_env()
environment={"EULA":"TRUE","TYPE":"FORGE","VERSION":"1.16.5","FORGEVERSION":"36.1.32","ONLINE_MODE":"FALSE"}
def createContainer(path,servername,port):
    container = dockerClient.containers.run(image="itzg/minecraft-server", name=servername,ports={'25565/tcp': port},
    environment=environment,volumes={path:{'bind':'/data','mode': 'rw'}},
    detach=True)
    return f'{container.short_id} Container created successful'
def removeContainer(servername):
    try:
        dockerClient.api.stop(servername)
        dockerClient.api.remove_container(servername)
        return True
    except:
        return False
def restartContainer(servername):
    try:
        dockerClient.api.restart(servername)
        return True
    except:
        return False
def startContainer(servername):
    try:
        dockerClient.api.start(servername)
        return True
    except:
        return False
def stopContainer(servername):
    try:
        dockerClient.api.stop(servername)
        return True
    except:
        return False
def listContainer():
    list = []
    containerList =  dockerClient.containers.list(all=True,filters={"ancestor":["itzg/minecraft-server"]})
    for item in containerList:
        containerInfo = dockerClient.containers.get(item.id)
        ports = containerInfo.attrs['HostConfig']['PortBindings'].items()
        finalPort = 0
        for key, value in ports:
            finalPort = value[0]['HostPort']
        list.append({'name':item.name,'status':item.status,'port':f"{finalPort}"})
    return list


