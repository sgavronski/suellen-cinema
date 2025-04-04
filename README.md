
# Projeto Cinema da Suellen.

Projeto para testar os conhecimentos de Python. Neste projeto vamos criar uma API para receber dados, processa-los e salva-los no bando de dados.

Pre-requisitos:
 - Linguagem Python.
 - Banco de dados MariaDB.
 - Framework FastAPI.

## Anotações
 - Instalar fastAPI `pip install "fastapi[standard]"`
 - Iniciar Programa Web: `fastapi dev main.py`
 - Encerrar Programa Web: precione ctrl+C no terminal.
 - Iniciar Programa Web (Debug): Licar no botão verde do inseto (debug) com a classe `main.py` selecionada no PyCharm.
 - Instalar MySQL no Python: `pip install mysql-connector-python`
 - Criar Docker do MariaDB: `docker run --detach --name mariadb --publish 3306:3306 --env MARIADB_ROOT_PASSWORD=pudim1234  mariadb:10.6`
 - Instalar biblioteca de teste: `pip install httpx`

## Operações GIT
 - Verificar status dos arquivos: `git status`
 - Adicionar arquivos novos e alterados: `git add .`
 - Adicionar arquivo especifico: `git add meu-arquivo.py`
 - Salvar arquivos no git: `git commit -m "Meu comentario do que fiz aqui."`
 - Publicar arquivos no Github: `git push origin main`
 - Puxar atualizações do GitHub: `git pull`

## Parte 1

 - Instalar Python3
 - Instalar MariaDB
 - Instalar Insomnia
 - Criar projeto Python com FastAPI.
 - Criar um Endpoint Hello World.