from fastapi import APIRouter, Body

from cadastro_veiculos.modulos import veiculos as vcl
from cadastro_veiculos.models.veiculos import (
    CriarVeiculoRequest,
    CriarVeiculoResponse,
    CRIAR_VEICULO_DEFAULT_RESPONSES,
)

router = APIRouter()


@router.post(
    "/veiculos",
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
