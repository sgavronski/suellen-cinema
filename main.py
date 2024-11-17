from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from person import Person
from filme import Filme
from database import Database
import classes


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

@app.get ('/mult')
async def mult (num1 : int, num2 : int):
    mult = num1 * num2
    return f'Multiplicação de {num1} por {num2}: {mult}'

@app.get('/start')
async def start():
    return classes.start()

@app.post('/person')
async def person(person: Person):
    was_added = app_database.add_person(person)
    if was_added:
        return f'Person {person.name} saved!'
    else:
        return f'Person not saved! Name is null.'

@app.post('/filme')
async def filme (filme: Filme):
    if app_database.add_filme(filme):
        return f'Filme {filme.titulo} adicionado com sucesso'
    else:
        return "Filme não adicionado pois não possui título"

@app.get('/person')
async def person(index: int):
    people_size = app_database.people_size()
    if people_size <= index:
        return "Pessoa nao existe na lista."
    else:
        return app_database.get_person(index)

@app.get('/filme')
async def filme(index: int):
    films_size = app_database.films_size()
    if films_size <= index:
        return "Filme não encontrado"
    else:
        return app_database.get_film(index)

@app.put('/person')
async def person(person: Person):
    was_updated = app_database.update_person(person)
    if was_updated:
        return f'Person {person.name} updated!'
    else:
        return f'Person not updated! Name is null or does not exist.'

@app.delete('/person')
async def person(index: int):
    people_size = app_database.people_size()
    if people_size <= index:
        return "Pessoa nao existe na lista."
    else:
        app_database.delete_person(index)
        return "Pessoa excluida."

@app.delete('/filme')
async def filme(index: int):
    films_size = app_database.films_size()
    if films_size <= index:
        return "Filme não encontrado. Digite outro parâmetro"
    else:
        app_database.delete_film(index)
        return "Filme Excluído com sucesso"

@app.get('/people')
async def people():
    return app_database.get_people()


@app.get('/movies')
async def movies():
    return app_database.getallmovies()





