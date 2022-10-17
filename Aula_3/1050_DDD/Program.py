from Interface_usuario import Interface_usuario
from Destino_repository import Destino_repository
from Leitor import adicionar_destinos

repositorio = Destino_repository()
interface = Interface_usuario(repositorio)
adicionar_destinos("destinos.txt",repositorio)

print(interface.saida_usuario())
print(interface.exibir_destinos())