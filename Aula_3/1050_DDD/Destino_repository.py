from Destino import Destino

class Destino_repository:
        lista_destino: Destino = []

        def __init__(self) -> None:
            pass

        def checa_se_destino_existe(self,destino:Destino) -> bool:
            for item in self.lista_destino:
                if (destino.DDD == item.DDD) or (destino.Destino == item.Destino):
                    return True
            return False

        def adicioanar_destino(self, destino:Destino) -> bool:
            if not self.checa_se_destino_existe(destino):
                self.lista_destino.append(destino)
                return True
            return False

        def obter_destino_pelo_ddd(self,ddd:int) -> str:
            for item in self.lista_destino:
                if item.DDD == ddd: 
                    return item.Destino
             
            return "Não encontrado"

        def __str__(self) -> str:
            formatText = "{0:<5} {1:<0}\n"
            menu = formatText.format("DDD:", "Localidade:")       
            
            for item in self.lista_destino:
                menu += formatText.format(item.DDD, item.Destino)
            
            return menu

