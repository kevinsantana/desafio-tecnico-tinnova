from cadastro_veiculos.database.veiculos import Veiculos


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
    """
    id = Veiculos(
        veiculo=veiculo,
        marca=marca,
        ano=ano,
        descricao=descricao,
        vendido=vendido,
    ).inserir()
    return id
