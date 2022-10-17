from Destino import Destino
from Destino_repository import Destino_repository

def pegar_destinos(local_arquivo:str) -> list:
    arq = open(local_arquivo, mode="r", encoding="utf-8")
    
    lista = []

    for linha in arq.readlines():
        lista.append(linha.replace("\n","").split(","))

    return lista


def adicionar_destinos(local_arquivo:str,repositorio:Destino_repository) -> None:

    arq = pegar_destinos(local_arquivo)
    for item in arq:
        repositorio.adicioanar_destino(Destino(int(item[0]),item[1]))