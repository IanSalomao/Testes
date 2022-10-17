from Destino_repository import Destino_repository
from Destino import Destino

class Interface_usuario:
    def __init__(self,destino_repository:Destino_repository) -> None:
        self.destino_repository = destino_repository

    def solicitar_input_usuario(self) -> str:
        ddd = int(input("Imforme o DDD: "))
        localidade = str(input("Informe a localidade: "))
        destino = Destino(ddd,localidade)

        if not self.destino_repository.adicioanar_destino(destino):
            return "Esse destino ou ddd já existe\n"
        return "Destino adicionado\n"

    def exibir_destinos(self) -> list:
        return self.destino_repository
        
    def saida_usuario(self) -> str:
        ddd = int(input("Imforme o DDD: "))
        
        return (f"DDD: {ddd}\nDestino: {self.destino_repository.obter_destino_pelo_ddd(ddd)}\n")

