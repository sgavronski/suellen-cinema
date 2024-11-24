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


@app.post('/pessoa')
async def pessoa(pessoa: Pessoa):
    adicionado = app_database.add_pessoa(pessoa)
    if adicionado:
        return f'Cadastro de {pessoa.nome} salvo!'
    else:
        return f'Cadastro não salvo! Nome nulo ou código de identificação nulo ou repetido.'


@app.post('/filme')
async def filme(filme: Filme):
    if app_database.adicionar_filme(filme):
        return f'Cadastro do filme {filme.titulo} adicionado com sucesso.'
    else:
        return "Filme não adicionado pois não possui título ou código inválido/nulo ou repetido"


@app.post('/locacao')
async def locacao(locacao_dto: Locacao_Dto): #criação de variável do tipo classe Locacao_dto
    adicionado = app_database.add_locacao(locacao_dto.cod_pessoa, locacao_dto.cod_filmes) #a função add_locacao recebe 2 variaveis: cod_pessoa e cod_filmes da classe Locacao_dto
    if adicionado:
        return f'Locacao {locacao.id} adicionado com sucesso'

    return "Locacao não adicionado pois não possui Pessoa ou Filmes."


@app.get('/pessoa')
async def pessoa(id_pessoa: int):
    return app_database.buscar_pessoa(id_pessoa)


@app.get('/filme')
async def filme(id_filme: int):
    return app_database.buscar_filme(id_filme)


@app.get('/locacao')
async def locacao(id: int):
    locacao = app_database.get_locacao(id)
    if locacao is None:
        return "Locacao nao encontrada."

    return locacao


@app.put('/pessoa')
async def pessoa(pessoa: Pessoa):
    atualizado = app_database.atualizar_pessoa(pessoa)
    if atualizado:
        return f'Pessoa {pessoa.nome} atualizada!'
    else:
        return f'Pessoa nao atualizada! Erro no código ou nome'


@app.put('/filme')
async def filme(filme: Filme):
    filmeatt = app_database.atualizar_filme(filme)
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
async def pessoa(id_pessoa: int):
    pessoa_deletada = app_database.deletar_pessoa(id_pessoa)
    if pessoa_deletada:
        return "Cadastro excluído."
    else:
        return "Cadastro não excluído. Código de identificação não encontrado"


@app.delete('/filme')
async def filme(id_filme: int):
    filme_deletado = app_database.deletar_filme(id_filme)
    if filme_deletado:
        return "Filme excluído com sucesso"
    else:
        return "Filme não excluído. Código de identificação não encontrado"

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
