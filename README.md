# minecraft-server-dockermanager

This is my vacation project to play minecraft server JAVA EDITION with my friends without fights.

# ENGLISH README

How does it work?

In order for minecraft java edition server's communication with the operating system to work, we need some point in between. So we use a python socket server to send commands to the operating system's command interface. And in minecraft, we create a connection between the connected player, and the python socket server. The game administrator will use the /docker <command args> command to execute the docker commands.
  But, this is a critical security issue. At this point, you can type "/docker shutdown" and the server will be shut down. We need to sanitize the commands and block any non-docker commands. 

This project is under construction. Dont use this in production.


# Português README

Este é o meu projeto de férias para jogar minecraft com meus amigos sem brigas.

Como funciona?

Para que a comunicação do servidor minecraft java edition com o sistema operacional funcione, precisamos de algum ponto entre os dois. Então, usamos um servidor de soquete em python para enviar comandos para a interface de comando do sistema operacional. E no minecraft, criamos uma conexão entre o jogador conectado, e o servidor de socket do python. O administrador do jogo usará o comando / docker <args de comando> para executar os comandos do docker. 
 Mas, esse é um problema de segurança crítico. Neste momento, você pode escrever "/docker shutdown" e o servidor será encerrado. Precisamos higienizar os comandos e barrar qualquer comando que não seja do docker. 

Este projeto está em construção. Não use isso na produção. 
