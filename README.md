# minecraft-server-dockermanager
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/brutalzinn/minecraft-server-dockermanager/blob/master/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/brutalzinn/minecraft-server-dockermanager/blob/master/README.pt.md)

This is my vacation project to play minecraft server JAVA EDITION with my friends without fights.

How does it work?

In order for minecraft java edition server's communication with the operating system to work, we need some point in between. So we use a python socket server to send commands to the operating system's command interface. And in minecraft, we create a connection between the connected player, and the python socket server. The game administrator will use the /docker <command args> command to execute the docker commands.
But, this is a critical security issue. At this point, you can type "/docker shutdown" and the server will be shut down. We need to sanitize the commands and block any non-docker commands.
This project is under construction. Dont use this in production.

