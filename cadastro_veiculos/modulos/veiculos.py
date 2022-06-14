from loguru import logger

from cadastro_veiculos.config import envs
from cadastro_veiculos.database.veiculos import Veiculos

from cadastro_veiculos.excecoes import ErrorDetails
from cadastro_veiculos.excecoes.veiculos import MarcaNaoExisteException


def validar_marca(marca: str) -> bool:
    """
    Valida se a marca informada existe.

    :param str marca: Marca a ser validada.
    :return: Se a marca é ou não valida.
    :rtype: bool
    """
    marcas = set(envs.MARCAS.lower().split(","))
    if marca.lower() in marcas:
        return True
    return False


def inserir(*, veiculo: str, marca: str, ano: int, descricao: str, vendido: bool):
    """
    Insere um novo veículo no banco de dados.

    :param str veiculo: Nome do veículo. Por exemplo: 'Civic'.
    :param str marca: Marca do veículo. Por exemplo: 'Honda'.
    :param int ano: Ano do carro. Por exemplo: '2022'
    :param str descricao: Descrição do carro. Por exemplo: 'sedan esportivo'
    :param bool vendido: Indicação se o veículo foi ou não vendido.
    :return: Id do veículo inserido.
    :rtype: int
    :raises MarcaNaoExisteException: A marca informada é inválida ou não existe.
    """
    if not validar_marca(marca):
        raise MarcaNaoExisteException(
            status=400,
            error="Bad Request",
            message="Marca inválida",
            error_details=[
                ErrorDetails(
                    message=f"A marca informada {marca} é inválida ou não existe."
                ).to_dict()
            ],
        )

    id = Veiculos(
        veiculo=veiculo,
        marca=marca,
        ano=ano,
        descricao=descricao,
        vendido=vendido,
    ).inserir()
    return id


def listar():
    total, veiculos = Veiculos().listar_todos()
    return total, veiculos


def buscar(marca: str = None, ano: int = None, vendido: bool = None):
    if not all([marca, ano, vendido]):
        pass
    total, veiculos = Veiculos(marca=marca, ano=ano, vendido=vendido).buscar()
    return total, veiculos


def buscar_um(id_veiculos: int):
    if not Veiculos(id_veiculos=id_veiculos).existe():
        pass
    return Veiculos(id_veiculos=id_veiculos).listar_um().dict()


def deletar(id_veiculos: int):
    if not Veiculos(id_veiculos=id_veiculos).existe():
        pass
    return Veiculos(id_veiculos=id_veiculos).deletar()
