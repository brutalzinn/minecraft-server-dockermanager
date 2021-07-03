import docker

dockerClient = docker.from_env()
environment = {"EULA":"TRUE"}
#dockerClient.containers.run(image="itzg/minecraft-server", command="-e EULA=TRUE -p 25565:25565", ports={'25565': 25565},environment=environment)
dockerClient.containers.run(image="itzg/minecraft-server", command="-e EULA=TRUE -p 25565:25565 --name mc",environment=environment)
#docker run -d -it docker run -d -it -p 25565:25565 -e EULA=TRUE -v /home/robertocpaes/minecraft-server:/data itzg/minecraft-server -p 25565:25565 -e EULA=TRUE itzg/minecraft-server