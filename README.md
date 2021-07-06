# minecraft-server-dockermanager
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/brutalzinn/minecraft-server-dockermanager/blob/master/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/brutalzinn/minecraft-server-dockermanager/blob/master/README.pt.md)

This is my vacation project to play minecraft server JAVA EDITION with my friends without fights.
# What it is?

It's a bungeecord plugin that can handle docker containers. We are using docker api with python. You can read about docker api here: [Access docker api documentation](https://docs.docker.com/engine/api/sdk/)


# How does it work?

We are using Python to communicate with docker api and to start a multi client socket server. The minecraft-server-dockermanager plugin sends socket messages to python socket server.
With these operation, we can manage docker containers. You can create a minecraft server 1.16.5 forge 36.1.32 modded called bananaServer on port 25565
with command /docker create bananaServer 25565 forge 1.16.5 36.1.32

# Requirements:

1. Python 3.x
2. Java SDK 8.x ( cant be newers java versions )
3. A development interface( Eclipse, IntelliJ IDEA. I recommend these two because you can find cool tutorials to start develop mods to minecraft easily)
4. Docker installed

# Setup

1. You need to pull itzg/minecraft-server image to your docker.
> docker pull itzg/minecraft-server
2. You need to docker pull itzg/bungeecord image to your docker.
> docker pull itzg/bungeecord

# Generating IDE Launch/Run Configurations:

### Read bungecoord plugin api at [Acess bungeecord plugin development](https://www.spigotmc.org/wiki/create-your-first-bungeecord-plugin-proxy-spigotmc/#making-it-load)


# A fluxogram of minecraft docker manager plugin

![Flow](https://raw.githubusercontent.com/brutalzinn/minecraft-server-dockermanager/master/images/docker_manager_flow.png)

# In any minecraft server container

### Typing /docker list to show all servers
![Print 1](https://raw.githubusercontent.com/brutalzinn/minecraft-server-dockermanager/master/images/print1.png)
### Creating a minecraft forge 36.1.32 server for minecraft 1.16.5
![Print 2](https://raw.githubusercontent.com/brutalzinn/minecraft-server-dockermanager/master/images/print2.png)
