from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Testa se o servidor web esta UP!
@app.get("/")
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

# Exemplo input\lendo mais de uma variavel.
@app.get("/read2values")
async def read2values(var1: str = "", var2: int = 0):
    soma = 10 + var2
    return "Exemplo de read de texto: " + var1 + " soma = " + str(soma)
