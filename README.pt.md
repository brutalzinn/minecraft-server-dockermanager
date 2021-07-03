# Multilanguage README Pattern
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/brutalzinn/minecraft-server-dockermanager/blob/master/README.md)

Este é o meu projeto de férias para jogar minecraft com meus amigos sem brigas.

Como funciona?

Para que a comunicação do servidor minecraft java edition com o sistema operacional funcione, precisamos de algum ponto entre os dois. Então, usamos um servidor de soquete em python para enviar comandos para a interface de comando do sistema operacional. E no minecraft, criamos uma conexão entre o jogador conectado, e o servidor de socket do python. O administrador do jogo usará o comando / docker <args de comando> para executar os comandos do docker.
Mas, esse é um problema de segurança crítico. Neste momento, você pode escrever "/docker shutdown" e o servidor será encerrado. Precisamos higienizar os comandos e barrar qualquer comando que não seja do docker.

Este projeto está em construção. Não use isso na produção. 