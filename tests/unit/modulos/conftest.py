from dataclasses import dataclass


@dataclass()
class Veiculos:
    veiculo: str = "Civic"
    marca: str = "Honda"
    ano: int = "2022"
    descricao: str = "Sedan esportivo"
    vendido: bool = False

    def existe(self):
        return False

    def inserir(self):
        return 1

    def atualizar(self):
        return True

    def deletar(self):
        return True

    def buscar(self):
        return self

    def dict(self):
        return self.__dict__

    def listar_todos(self):
        return [self.__dict__, self.__dict__]


@dataclass()
class VeiculosBuscarNaoExiste:
    veiculo: str = "Civic"
    marca: str = "Honda"
    ano: int = "2022"
    descricao: str = "Sedan esportivo"
    vendido: bool = False

    def existe(self):
        return False

    def buscar(self):
        return False

    def dict(self):
        return self.__dict__
