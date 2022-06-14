from fastapi import APIRouter, Body, Query, Path

from cadastro_veiculos.modulos import veiculos as vcl
from cadastro_veiculos.models.veiculos import (
    CriarVeiculoRequest,
    CriarVeiculoResponse,
    CRIAR_VEICULO_DEFAULT_RESPONSES,
)

router = APIRouter()


@router.post(
    "/",
    status_code=201,
    summary="Cadastrar um veículo",
    response_model=CriarVeiculoResponse,
    responses=CRIAR_VEICULO_DEFAULT_RESPONSES,
)
def criar(
    veiculo: CriarVeiculoRequest = Body(
        ..., description="Dados básicos para cadastro de um novo veículo"
    )
):
    """
    Enpoint para criar um novo veículo.
    """
    return {"id": vcl.inserir(**veiculo.dict())}


@router.get(
    "/",
    status_code=200,
    summary="Listar os veículos da base",
)
def list_all():
    """
    Endpoint para listar os veículos da base.
    """
    _, veiculos = vcl.listar()
    return {"veiculos": veiculos}


@router.get(
    "",
    status_code=200,
    summary="Buscar veículos.",
)
def buscar(
    marca: str = Query("Honda", description="Marca do(s) veículo(s) buscado(s)"),
    ano: int = Query(2022, description="Ano do(s) veículo(s) buscado(s)"),
    vendido: bool = Query(False, description="Se o veículo consta ou não como vendido"),
):
    """
    Enpoint para buscar veículos.
    """
    _, veiculos = vcl.buscar(marca, ano, vendido)
    return {"veiculos": veiculos}


@router.get(
    "/{id_veiculos}",
    status_code=200,
    summary="Buscar um veículo.",
)
def buscar_um(
    id_veiculos: int = Path(1, description="Id do veículo buscado"),
):
    """
    Enpoint para buscar um veículo.
    """
    return {"veiculos": vcl.buscar_um(id_veiculos)}


@router.delete(
    "/{id_veiculos}",
    status_code=200,
    summary="Deleta um veículo",
)
def deletar(
    id_veiculos: int = Path(1, description="Id do veículo"),
):
    """
    Enpoint para deletar um veículo.
    """
    return {"resultado": vcl.deletar(id_veiculos)}
