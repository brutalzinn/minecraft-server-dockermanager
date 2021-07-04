# minecraft-server-dockermanager
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/brutalzinn/minecraft-server-dockermanager/blob/master/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/brutalzinn/minecraft-server-dockermanager/blob/master/README.pt.md)

This is my vacation project to play minecraft server JAVA EDITION with my friends without fights.
This project needs [Minecraft server docker image](https://github.com/itzg/docker-minecraft-server)
# What it is?

It's a minecraft mod that can handle docker containers. We are using docker api with python. You can read about docker api here: [Access docker api documentation](https://docs.docker.com/engine/api/sdk/)

# Single-player or multiplayer mod?

At this moment, it's only single-player mod. But this mod needs be runs only on server side.

This project was started on Jul 2, 2021. And its not ready to be used without dev mode.

# How does it work?

We are using Python to communicate with docker api and to start a multi client socket server. The minecraft mod send socket messages to Python server.
With these operation, we can manage docker containers. You can create a minecraft server 1.16.5 forge modded called bananaServer on port 25565
with command /docker create bananaServer 25565

# Requirements:

1. Python 3.x
2. Java SDK 8.x ( cant be newers java versions )
3. A development interface( Eclipse, IntelliJ IDEA. I recommend these two because you can find cool tutorials to start develop mods to minecraft easily)
4. Read about forge api( this is can help you for setup )  [Access forge api documentation](https://mcforge.readthedocs.io/en/latest/gettingstarted/#building-and-testing-your-mod)
5. A minecraft client with forge-1.16.5-36.1.32 installed
6. Docker installed

# Config setup

1. You need to pull itzg/minecraft-server image to your docker.
> docker pull itzg/minecraft-server

Generating IDE Launch/Run Configurations:

You can find the full setup here: [Access forge getting started](https://mcforge.readthedocs.io/en/latest/gettingstarted/#building-and-testing-your-mod)

For Eclipse, run the genEclipseRuns gradle task (gradlew genEclipseRuns). This will generate the Launch Configurations and download any required assets for the game to run. After this has finished, refresh your project.

For IntelliJ, run the genIntellijRuns gradle task (gradlew genIntellijRuns). This will generate the Run Configurations and download any required assets for the game to run. If you encounter an error saying “module not specified”, you can either edit the configuration to select your “main” module or specify it through the ideaModule property.


What i need to do to run this?