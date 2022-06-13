from datetime import datetime
from dataclasses import dataclass

from cadastro_veiculos.database import DataBase, campos_obrigatorios


@dataclass
class Veiculos(DataBase):
    id: int = None
    veiculo: str = None
    marca: str = None
    ano: int = None
    descricao: str = None
    vendido: bool = False
    created: datetime = None
    updated: datetime = None

    @property
    def veiculo(self):
        return self.__veiculo

    @property
    def marca(self):
        return self.__marca

    @property
    def ano(self):
        return self.__ano

    @property
    def descricao(self):
        return self.__descricao

    @property
    def vendido(self):
        return self.__vendido

    @property
    def created(self):
        return self.__created

    @property
    def updated(self):
        return self.__updated

    def dict(self):
        return {
            key.replace("_Veiculo__", ""): value
            for key, value in self.__dict__.items()
            if value
        }

    @campos_obrigatorios(["veiculo", "marca", "ano", "descricao", "vendido"])
    def inserir(self):
        """
        Insere um veículo no banco de dados.

        :param str veiculo: Nome do veículo. Por exemplo: 'Civic'.
        :param str marca: Marca do veículo. Por exemplo: 'Honda'.
        :param int ano: Ano do carro. Por exemplo: '2022'
        :param str descricao: Descrição do carro. Por exemplo: 'sedan esportivo'
        :param bool vendido: Indicação se o veículo foi ou não vendido.
        :return: Id do veículo inserido.
        :rtype: int
        """
        self.query_string = """INSERT INTO VEICULOS (VEICULO, MARCA, ANO, DESCRICAO, VENDIDO, CREATED)
        values (%(veiculo)s, %(marca)s, %(ano)s, %(descricao)s, %(vendido)s, current_timestamp)"""
        return self.insert()

    @campos_obrigatorios(["id"])
    def atualizar(self):
        """
        Atualiza um veículo.

        :param int id: Id do veículo.
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = """
        UPDATE VEICULOS SET VEICULO=%(veiculo)s, MARCA=%(marca)s, ANO=%(ano)s, DESCRICAO=%(descricao)s,
        VENDIDO=%(vendido)s, UPDATED=current_timestamp
        """
        self.query_string += " WHERE VEICULOS.ID = %(id)s"
        return True if self.insert() else False

    @campos_obrigatorios(["id"])
    def existe(self):
        """
        Verifica se um veículo existe no banco de dados.

        :param int id: Id do veículo.
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = "SELECT COUNT(*) FROM VEICULOS WHERE VEICULOS.ID = %(id)s"
        return True if self.find_one()[0] else False

    @campos_obrigatorios(["id"])
    def deletar(self):
        """
        Deleta um veículo do banco de dados.

        :param int id: Id do veículo.
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = "DELETE FROM VEICULOS WHERE VEICULOS.ID = %(id)s"
        return True if self.insert() else False

    def buscar(self):
        """
        Busca, a partir dos parâmetros informados, veículos.

        :param marca: Marca dos veículos buscados.
        :type marca: str, optional
        :param ano: Ano dos veículos buscados.
        :type ano: int, optional
        :vendido: Filtrar entre veículos vendidos ou não.
        :type vendido: bool, optional
        """
        self.query_string = """
        SELECT * FROM VEICULOS
        WHERE VEICULOS.MARCA = %()s, VEICULOS.ANO = %()s, VEICULOS.VENDIDO = %()s
        """
        veiculos, total = self.find_all(total=True)
        return total, [Veiculos(**dict(veiculo)) for veiculo in veiculos]
