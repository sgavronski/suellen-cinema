import uvicorn
from typing import List
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from database import Database
from filme import Filme
from pessoa import Pessoa


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
        return f"Cadastro de {pessoa.nome}, código *{pessoa.id_pessoa}* adicionado com sucesso"
    else:
        return "ERRO! Cadastro não realizado"


@app.post('/filme')
async def filme(filme: Filme):
    if app_database.adicionar_filme(filme):
        return f'Cadastro do filme {filme.titulo}, código *{filme.id_filme}* adicionado com sucesso.'
    else:
        return "Filme não adicionado pois não possui título ou código inválido/nulo ou repetido"


@app.post('/locacao')
#async def locacao(cod_pessoa: int, cod_filmes: int):
async def locacao(cod_pessoa: int, cod_filmes: List[int] = Query(None)):
    locacao_adicionada = app_database.adicionar_locacao(cod_pessoa, cod_filmes)
    idlo = app_database.ultima_locacao()

    if locacao_adicionada:
        return f"Locação código *{idlo}* adicionada com sucesso"
    else:
        return "Locação não efetuada"


@app.get('/pessoa')
async def pessoa(id_pessoa: int):
    return app_database.buscar_pessoa(id_pessoa)


@app.get('/filme')
async def filme(id_filme: int):
    return app_database.buscar_filme(id_filme)


@app.get('/locacao')
async def locacao(id: int):
    return app_database.buscar_locacao(id)


@app.put('/pessoa')
async def pessoa(pessoa: Pessoa):
    atualizado = app_database.atualizar_pessoa(pessoa)
    if atualizado:
        return f'Cadastro de {pessoa.nome} atualizado!'
    else:
        return f'Pessoa nao atualizada! Código não equivale a nenhuma pessoa ou nome não preenchido'


@app.put('/filme')
async def filme(filme: Filme):
    filmeatt = app_database.atualizar_filme(filme)
    if filmeatt:
        return f'Filme {filme.titulo} atualizado com sucesso'
    else:
        return "Filme não atualizado! Código não equivale a nenhum filme ou título não preenchido"


@app.put('/locacao')
async def locacao(id: int = Query(None), cod_pessoa: int = Query(None), cod_filmes: List[int] = Query(None)):
    if id is None:
        return "Falta id da locação"
    elif cod_pessoa is None:
        return "Falta codigo da pessoa"
    elif cod_filmes is None:
        return "Falta código de filme"

    atualizado = app_database.atualizar_locacao(id, cod_pessoa, cod_filmes)
    if atualizado:
        return f'Locacao atualizado com sucesso'
    else:
        return "Locacao não foi atualizado pois a) não foi encontrada, b) cliente não encontrado, c) filmes não encontrados, d)já foi finalizada"


@app.delete('/pessoa')
async def pessoa(id_pessoa: int):
    pessoa_deletada = app_database.deletar_pessoa(id_pessoa)
    if pessoa_deletada:
        return "Cadastro excluído."
    else:
        return ("Cadastro não excluído. Possíveis motivos: "
                "a) Código de identificação não encontrado "
                "b) Registro de pessoa incluído em uma ou mais locações não permite sua exclusão ")


@app.delete('/filme')
async def filme(id_filme: int):
    filme_deletado = app_database.deletar_filme(id_filme)
    if filme_deletado:
        return "Filme excluído com sucesso"
    else:
        return ("Filme não excluído. Possíveis motivos: "
                "a) Código de identificação não encontrado"
                "b) Registro de filme incluído em uma ou mais locações não permite sua exclusão")

@app.delete('/locacao')
async def locacao(id: int):
    deletado = app_database.delete_locacao(id)
    if deletado:
        return "Locacao excluída com sucesso"
    else:
        return "Locação não excluída pois não foi encontrada ou já foi finalizada"


@app.get('/pessoas')
async def pessoas():
    return app_database.get_todas_pessoas()


@app.get('/filmes')
async def filmes():
    return app_database.get_todos_filmes()

@app.get('/locacoes')
async def locacoes():
    return app_database.get_todas_locacoes()

@app.post('/devolucao')
async def devolucao(id_locacao: int, data_devolucao: str):
    dev_efetuada = app_database.fazer_devolucao(id_locacao, data_devolucao)
    if dev_efetuada:
        return "Devolução efetuada"
    else:
        return "Devolução não efetuada"

@app.post('/pagamento')
async def pagamento (id_locacao: int, forma_pagamento: str, valorpago: float):
    pag_efetuado = app_database.efetuar_pagamento(id_locacao, forma_pagamento, valorpago)
    if pag_efetuado:
        return "Pagamento efetuado"
    else:
        return "Pagamento não concluído. Locação não encontrada ou valor digitado maior que o débito ou pagamento nulo"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
