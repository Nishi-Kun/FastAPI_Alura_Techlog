from fastapi import APIRouter # importa da biblioteca fastapi a função APIRouter, que será utilizada para criar rotas;
from app.modelos.clientes import Cliente # importando do arquivo "clientes.py" a classe Cliente

CLIENTS_LIST = [Cliente(id_=1,nome="Francisco",email="email2@email.com",telefone="40028923"),
                Cliente(id_=2,nome="Erik",email="email2@email.com",telefone="40028923")]

#variável que guarda uma lista de clientes, Cada ítem da lista é uma instância da classe Cliente, que contém os atributos descritos.

router = APIRouter( #Uma variável que guarda a instância da APIRouter, com o prefixo(rota) /clientes.
    prefix="/clientes"
)

@router.get("/",response_model = list[Cliente]) #cria uma rota do tipo "GET", endereçando a rota "/" dizendo que o modelo de resposta esperada para ela é uma lista do tipo "Classe Cliente"
async def listar_clientes():
    return CLIENTS_LIST # uma função assíncrona que retorna uma lista com todos os clientes armazenados nessa varíavel.


@router.get("/{cliente_id}",response_model=Cliente | None) #cria uma rota que recebe um parâmetro, e que espera um modelo de resposta do tipo "Classe Cliente"
async def obter_cliente(cliente_id: int):
    for cliente in CLIENTS_LIST:
        if cliente.id_ == cliente_id:
            return cliente
    return None
