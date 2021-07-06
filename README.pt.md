# minecraft-server-dockermanager

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/brutalzinn/minecraft-server-dockermanager/blob/master/README.md)

Este é o meu projeto de férias para jogar minecraft server JAVA EDITION com meus amigos sem brigas.
# O que é isso?

É um plug-in bungeecord que pode lidar com contêineres do docker. Estamos usando docker api com python. Você pode ler sobre a docker api aqui: [Acessar a documentação da docker api](https://docs.docker.com/engine/api/sdk/)


# Como funciona?

Estamos usando Python para nos comunicarmos com a docker api e para iniciar um servidor de soquete de múltiplos clientes. O plug-in minecraft-server-dockermanager envia mensagens de soquete para o servidor de soquete python.
Com essas operações, podemos gerenciar os contêineres docker. Você pode criar um servidor de minecraft 1.16.5 forge 36.1.32 modificado chamado bananaServer na porta 25565
com comando /docker create bananaServer 25565 forge 1.16.5 36.1.32

# Requisitos:

1. Python 3.x
2. Java SDK 8.x (não pode ser versões Java mais recentes)
3. Uma interface de desenvolvimento (Eclipse, IntelliJ IDEA. Recomendo esses dois porque você pode encontrar tutoriais interessantes para começar a desenvolver mods para minecraft facilmente)
4. Docker instalado

# Configuração

1. Você precisa puxar a imagem itzg/minecraft-server para o docker.
> docker pull itzg/minecraft-server
2. Você precisa puxar a imagem itzg/bungeecord na janela de encaixe.
> docker pull itzg/bungeecord

# Gerando configurações de inicialização / execução do IDE:

### Leia sobre desenvolvimento de plugins para o bungeecord em [Acessar documentação de inicialização](https://www.spigotmc.org/wiki/create-your-first-bungeecord-plugin-proxy-spigotmc/#making-it-load)

# Fluxograma para o Bungeecord dockermanager plugin

![Flow](https://raw.githubusercontent.com/brutalzinn/minecraft-server-dockermanager/master/images/docker_manager_flow.png)

# Dentro de qualquer container

### Digitando /docker list para mostrar todos os servidores criados
![Print 1](https://raw.githubusercontent.com/brutalzinn/minecraft-server-dockermanager/master/images/print1.png)
### Criando um servidor do minecraft forge 36.1.32 para o minecraft 1.16.5
![Print 2](https://raw.githubusercontent.com/brutalzinn/minecraft-server-dockermanager/master/images/print2.png)
