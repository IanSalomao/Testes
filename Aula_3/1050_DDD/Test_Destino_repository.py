from Destino import Destino
from Destino_repository import Destino_repository
from Leitor import adicionar_destinos

def test_ddd_detino():

    repositorio = Destino_repository()

    adicionar_destinos("./destinos.txt",repositorio)
    
    assert repositorio.adicioanar_destino(Destino(90,"Senai"))
    assert repositorio.obter_destino_pelo_ddd(90) == "Senai"


def test_len_repository():

    repositorio = Destino_repository()

    adicionar_destinos("./destinos.txt",repositorio)

    assert len(repositorio.lista_destino) == 10

