from loguru import logger

from cadastro_veiculos.config import envs
from cadastro_veiculos.database.veiculos import Veiculos

from cadastro_veiculos.excecoes import ErrorDetails
from cadastro_veiculos.excecoes.veiculos import (
    MarcaNaoExisteException,
    FiltroInvalidoException,
    VeiculoNaoEncontradoException,
    AtualizacaoInvalidaException,
)


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
    """
    Lista todos os veículos da base.

    :return: Lista de veículos.
    :rtype: list
    """
    total, veiculos = Veiculos().listar_todos()
    return total, veiculos


def buscar(marca: str = None, ano: int = None, vendido: bool = None):
    """
    Busca veículo(s) a partir do(s) filtro(s) informado(s).

    :param marca: Marca dos veículos buscados.
    :type marca: str, optional
    :param ano: Ano dos veículos buscados.
    :type ano: int, optional
    :vendido: Filtrar entre veículos vendidos ou não.
    :type vendido: bool, optional
    :return: Veiculos da base.
    :rtype: list
    :raises FiltroInvalidoException: Caso nenhum filtro seja informado.
    """
    if not all([marca, ano, vendido]):
        raise FiltroInvalidoException(
            status=400,
            error="Bad Request",
            message="Filtro inválido",
            error_details=[
                ErrorDetails(message="É preciso informar ao menos um filtro.").to_dict()
            ],
        )
    total, veiculos = Veiculos(marca=marca, ano=ano, vendido=vendido).buscar()
    return total, veiculos


def buscar_um(id_veiculos: int):
    """
    Busca um veículo a partir do id informado.

    :param int id_veiculos: Id do veículo buscado.
    :return: Veículo buscado.
    :rtype: dict
    :raises VeiculoNaoEncontradoException: Não foi encontrado um registro a partir do id informado.
    """
    if not Veiculos(id_veiculos=id_veiculos).existe():
        raise VeiculoNaoEncontradoException(
            status=404,
            error="Not Found",
            message="Registro não encontrado",
            error_details=[
                ErrorDetails(
                    message=f"Não foi encontrado um registro a partir do id informado {id_veiculos}."
                ).to_dict()
            ],
        )
    return Veiculos(id_veiculos=id_veiculos).listar_um().dict()


def atualizar(id_veiculos: int, dados_atualizacao: dict, parcial=False):
    """
    Atualiza um registro ou parte dele.

    :param int id_veiculos: Id do veículo que será atualizado.
    :param dict dados_atualizados: Dados a serem atualizados.
    :param parcial: Caso a atualização seja parcial.
    :type parcial: bool, optional
    :return: Indicação se o registro foi ou não atualizado com sucesso.
    :rtype: bool
    :raises VeiculoNaoEncontradoException: Não foram encontrado registros.
    :raises AtualizacaoInvalidaException: Não foram informados campos para a atualização.
    """
    if not Veiculos(id_veiculos=id_veiculos).existe():
        raise VeiculoNaoEncontradoException(
            status=404,
            error="Not Found",
            message="Registro não encontrado",
            error_details=[
                ErrorDetails(
                    message=f"Não foi encontrado um registro a partir do id informado {id_veiculos}."
                ).to_dict()
            ],
        )
    if not dados_atualizacao:
        raise AtualizacaoInvalidaException(
            status=400,
            error="Bad request",
            message="Atualização inválida",
            error_details=[
                ErrorDetails(
                    message="Não foram informados campos para a atualização do registro."
                ).to_dict()
            ],
        )
    return Veiculos(id_veiculos=id_veiculos, **dados_atualizacao.dict()).atualizar(
        parcial=parcial
    )


def deletar(id_veiculos: int):
    """
    Deleta um registro da base.

    :param int id_veiculos: Id do veículo que será atualizado.
    :return: Indicação se o registro foi ou não atualizado com sucesso.
    :rtype: bool
    :raises VeiculoNaoEncontradoException: Não foi encontrado um registro a partir do id informado.
    """
    if not Veiculos(id_veiculos=id_veiculos).existe():
        raise VeiculoNaoEncontradoException(
            status=404,
            error="Not Found",
            message="Registro não encontrado",
            error_details=[
                ErrorDetails(
                    message=f"Não foi encontrado um registro a partir do id informado {id_veiculos}."
                ).to_dict()
            ],
        )
    return Veiculos(id_veiculos=id_veiculos).deletar()
