#Arquivo principal do projeto:

from fastapi import FastAPI #importa a biblioteca principal para criação de API's
from fastapi.responses import HTMLResponse # importa da biblioteca "responses" uma subfunção, que permite retornar html na resposta da API.
from app.rotas import cliente #importa do arquivo "rota.apps" o arquivo "cliente.py"

app = FastAPI(                     #Guarda a instância do FastAPI na variável "app"
    title="Techlog API",           #O fast api recebe alguns atributos: Titulo, descrição e versão.
    description="Techlog CRM",
    version="1.0.0",
)

app.include_router(cliente.router) #utilize o método "include.router" da variável app, para chamar uma rota existente.

@app.get("/") #cria a rota(endpoint) "/", que pode ser chamada no navegador.
async def health_check(): #Ao buscar "/" na barra de endereço do navegador, é executada a função assíncrona.
    return {"status": "ok"}  #Esse é o retorno na página do navegador ao buscar este endpoint


@app.get("/front", response_class=HTMLResponse) #cria a rota(endpoint) "front", que pode ser chamada no navegador e definimos que a resposta dela será do tipo HTMLResponse
async def front():
    html_content = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Techlog CRM</title>
            </head>
            <body>
                <h1>Techlog CRM</h1>
                <p>Essa é a página inicial do Techlog CRM.</p>
                <p><strong>Status:</strong> Operacional</p>
            </body>
        </html>
    """ #Uma variável que guarda HTML;
    return html_content

