from pytest import MonkeyPatch
from Interface_usuario import Interface_usuario
from Destino_repository import Destino_repository
from Leitor import adicionar_destinos



def test_saida_usuario(monkeypatch):

    # Arrange
    repositorio = Destino_repository()
    interface = Interface_usuario(repositorio)

    # Act   
    adicionar_destinos("./destinos.txt",repositorio)
    monkeypatch.setattr('builtins.input', lambda _: 75)

    
    
    # Assert
    assert interface.saida_usuario() == "DDD: 75\nDestino: Bahia\n"
    

def test_solicitar_input_usuario(monkeypatch):

    # Arrange
    repositorio = Destino_repository()
    interface = Interface_usuario(repositorio)

    # Act   
    adicionar_destinos("./destinos.txt",repositorio)

    responses = iter([22,"Matinha",22])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    # Assert
    assert interface.solicitar_input_usuario() == "Destino adicionado\n"
    assert interface.saida_usuario() == "DDD: 22\nDestino: Matinha\n"