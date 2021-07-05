# minecraft-server-dockermanager

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/brutalzinn/minecraft-server-dockermanager/blob/master/README.md)

Este é o meu projeto de férias para jogar minecraft server JAVA EDITION com meus amigos sem brigas.
Este projeto precisa de [imagem docker do servidor do Minecraft] (https://github.com/itzg/docker-minecraft-server)
# O que é isso?

É um mod minecraft que pode lidar com contêineres docker. Estamos usando docker api com python. Você pode ler sobre a docker api aqui: [Acesse a documentação da docker api] (https://docs.docker.com/engine/api/sdk/)

# Mod para um jogador ou multijogador?

Neste momento, é apenas um mod para um jogador. Mas este mod precisa ser executado apenas no lado do servidor.

Este projeto foi iniciado em 2 de julho de 2021. E não está pronto para ser usado sem o modo dev.

# Como funciona?

Estamos usando Python para nos comunicarmos com a docker api e para iniciar um servidor de soquete de múltiplos clientes. O mod minecraft envia mensagens de soquete para o servidor Python.
Com essas operações, podemos gerenciar os contêineres docker. Você pode criar um servidor de minecraft 1.16.5 forge modificado chamado bananaServer na porta 25565
com command / docker criar bananaServer 25565

# Requisitos:

1. Python 3.x
2. Java SDK 8.x (não pode ser versões Java mais recentes)
3. Uma interface de desenvolvimento (Eclipse, IntelliJ IDEA. Recomendo esses dois porque você pode encontrar tutoriais interessantes para começar a desenvolver mods para minecraft facilmente)
4. Leia sobre a API do forge (isso pode ajudá-lo na configuração) [Acessar a documentação da API do forge] (https://mcforge.readthedocs.io/en/latest/gettingstarted/#building-and-testing-your-mod)
5. Um cliente minecraft com forge-1.16.5-36.1.32 instalado
6. Docker instalado

# Configuração

1. Você precisa puxar a imagem itzg / minecraft-server para o docker.
> docker pull itzg/minecraft-server

Gerando configurações de inicialização / execução do IDE:

Você pode encontrar a configuração completa aqui: [Access forge Getting started] (https://mcforge.readthedocs.io/en/latest/gettingstarted/#building-and-testing-your-mod)

Para Eclipse, execute a tarefa gradle genEclipseRuns (gradlew genEclipseRuns). Isso gerará as configurações de inicialização e fará o download de todos os ativos necessários para que o jogo seja executado. Depois de terminar, atualize seu projeto.

Para IntelliJ, execute a tarefa gradle genIntellijRuns (gradlew genIntellijRuns). Isso gerará as configurações de execução e fará o download de todos os recursos necessários para que o jogo seja executado. Se você encontrar um erro dizendo “módulo não especificado”, você pode editar a configuração para selecionar seu módulo “principal” ou especificá-lo através da propriedade ideaModule.

# In game

### Digitando /docker list para mostrar todos os servidores criados
![Print 1](https://raw.githubusercontent.com/brutalzinn/minecraft-server-dockermanager/master/print1.png)
### Criando um servidor do minecraft forge 36.1.32 para o minecraft 1.16.5
![Print 2](https://raw.githubusercontent.com/brutalzinn/minecraft-server-dockermanager/master/print2.png)
