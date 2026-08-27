from pydantic import BaseModel ## bliblioteca mais utilizada para validação de modelo de dados

class Cliente(BaseModel): 
    id_:int #usar id_ porque id já é um método built-in do python. Ele serve para mostrar o local na memória onde o valor está armazenado.
    nome:str
    email:str
    telefone:str
