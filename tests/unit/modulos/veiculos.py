from unittest.mock import patch

from tests.unit.modulos.conftest import Veiculos

from cadastro_veiculos.modulos.veiculos import inserir, listar


@patch("cadastro_veiculos.modulos.veiculos.inserir")
@patch("cadastro_veiculos.modulos.veiculos.Veiculos")
def test_inserir_veiculos_com_sucesso(mock_veiculos_db, mock_inserir_veiculos):
    mock_veiculos_db.return_value = Veiculos()
    assert inserir(**Veiculos().__dict__)


@patch("cadastro_veiculos.modulos.veiculos.listar")
@patch("cadastro_veiculos.modulos.veiculos.Veiculos")
def test_listar_todos_com_sucesso(mock_veiculos_db, mock_listar_veiculos):
    mock_veiculos_db.return_value = Veiculos()
    result = list(listar())
    assert isinstance(result, list) is True
