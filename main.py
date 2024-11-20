import uvicorn

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from locacao import Locacao
from locacao_dto import Locacao_Dto
from pessoa import Pessoa
from filme import Filme
from database import Database


app = FastAPI()
app_database = Database() #atribui ao app_database o database (classe)


# Testa se o servidor web esta UP!
@app.get("/") #essa linha é um decorator. É uma linha de código que atribui uma funcionalidade pra função que está logo abaixo dele quando entrar no link
async def root():
    return "Cinema Suellen UP!"


# Exemplo retornando uma pagina HTML.
@app.get("/html", response_class=HTMLResponse)
async def html():
    html = '<!DOCTYPE html> <html> <body> <h1>Cinema Suellen</h1> <p>Cinema da Suellen.</p> </body> </html>'
    return HTMLResponse(content=html, status_code=200)


# Exemplo output\imprimindo text.
@app.get("/print")
async def print():
    return "Exemplo de print de texto."


# Exemplo input\lendo text.
@app.get("/read")
async def read(texto: str = ""):
    return "Exemplo de read de texto: " + texto


#soma de dois numeros
@app.get ("/soma") #assinatura http
async def soma (num1: int =0, num2: int = 0):
    soma= num1 + num2
    return f'Resultado da soma das variáveis {num1} e {num2}: {soma}'


#cada assinatura corresponde a uma função
@app.get('/teste')
async def teste (nome: str, idade: int):
    return f'Nome do cliente: {nome}, Idade: {idade} anos'


@app.get('/mult')
async def mult (num1 : int, num2 : int):
    mult = num1 * num2
    return f'Multiplicação de {num1} por {num2}: {mult}'


@app.post('/pessoa')
async def pessoa(pessoa: Pessoa):
    adicionado = app_database.add_pessoa(pessoa)
    if adicionado:
        return f'pessoa {pessoa.name} salva!'
    else:
        return f'pessoa nao salva! Nome e nulo.'


@app.post('/filme')
async def filme(filme: Filme):
    if app_database.add_filme(filme):
        return f'Filme {filme.titulo} adicionado com sucesso'
    else:
        return "Filme não adicionado pois não possui título"


@app.post('/locacao')
async def locacao(locacao_dto: Locacao_Dto):
    adicionado = app_database.add_locacao(locacao_dto.cod_pessoa, locacao_dto.cod_filmes)
    if adicionado:
        return f'Locacao {locacao.id} adicionado com sucesso'

    return "Locacao não adicionado pois não possui Pessoa ou Filmes."


@app.get('/pessoa')
async def pessoa(index: int):
    pessoa_size = app_database.pessoa_size()
    if pessoa_size <= index:
        return "Pessoa nao existe na lista."
    else:
        return app_database.get_pessoa(index)


@app.get('/filme')
async def filme(index: int):
    films_size = app_database.films_size()
    if films_size <= index:
        return "Filme não encontrado"
    else:
        return app_database.get_film(index)


@app.get('/locacao')
async def locacao(id: int):
    locacao = app_database.get_locacao(id)
    if locacao is None:
        return "Locacao nao encontrada."

    return locacao


@app.put('/pessoa')
async def pessoa(pessoa: Pessoa):
    atualizado = app_database.update_pessoa(pessoa)
    if atualizado:
        return f'Pessoa {pessoa.name} atualizada!'
    else:
        return f'Pessoa nao atualizada! Codigo nao existe.'


@app.put('/filme')
async def filme(filme: Filme):
    filmeatt = app_database.update_filme(filme)
    if filmeatt:
        return f'Filme {filme.titulo} atualizado com sucesso'
    else:
        return "Filme não foi atualizado pois ou não possui título ou não foi encontrado"


@app.put('/locacao')
async def locacao(id: int, locacao: Locacao):
    atualizado = app_database.update_locacao(id, locacao)
    if atualizado:
        return f'Locacao {locacao.id} atualizado com sucesso'
    else:
        return "Locacao não foi atualizado pois não foi encontrado"


@app.delete('/pessoa')
async def pessoa(index: int):
    pessoa_size = app_database.pessoa_size()
    if pessoa_size <= index:
        return "Pessoa nao existe na lista."
    else:
        app_database.delete_pessoa(index)
        return "Pessoa excluida."


@app.delete('/filme')
async def filme(index: int):
    films_size = app_database.films_size()
    if films_size <= index:
        return "Filme não encontrado. Digite outro parâmetro"
    else:
        app_database.delete_film(index)
        return "Filme Excluído com sucesso"

@app.delete('/locacao')
async def locacao(id: int):
    deletedo = app_database.delete_locacao(id)
    if deletedo:
        return "Locacao Excluída com sucesso"
    else:
        return "Locacao não encontrado."


@app.get('/pessoas')
async def pessoas():
    return app_database.get_todas_pessoas()


@app.get('/filmes')
async def filmes():
    return app_database.get_todos_filmes()

@app.get('/locacoes')
async def locacoes():
    return app_database.get_todas_locacoes()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
