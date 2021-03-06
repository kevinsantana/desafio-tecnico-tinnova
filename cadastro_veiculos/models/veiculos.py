from typing import Optional
from pydantic import BaseModel, Field

from cadastro_veiculos.excecoes import ErrorDetails
from cadastro_veiculos.models import parse_openapi, Message


class CriarVeiculoRequest(BaseModel):
    veiculo: str = Field("Civic", description="Nome do veículo")
    marca: str = Field("Honda", description="Marca do veículo")
    ano: int = Field(2022, description="Ano do veículo")
    descricao: str = Field(
        "Sedan esportivo", description="Uma descrição sobre o veículo"
    )
    vendido: bool = Field(False, description="Indicar se o veículo foi ou não vendido")


class CriarVeiculoResponse(BaseModel):
    id: int


class AtualizarVeiculoRequest(BaseModel):
    veiculo: Optional[str] = Field(None, description="Nome do veículo")
    marca: Optional[str] = Field(None, description="Marca do veículo")
    ano: Optional[int] = Field(None, description="Ano do veículo")
    descricao: Optional[str] = Field(None, description="Uma descrição sobre o veículo")
    vendido: Optional[bool] = Field(
        None, description="Indicar se o veículo foi ou não vendido"
    )


class AtualizarVeiculoResponse(BaseModel):
    resultado: bool


CRIAR_VEICULO_DEFAULT_RESPONSES = parse_openapi(
    [
        Message(
            status=400,
            error="Bad Request",
            message="Campo inválido",
            error_details=[
                ErrorDetails(message="O campo informado é inválido").to_dict()
            ],
        ),
        Message(
            status=409,
            error="Conflict",
            message="Dado repetido",
            error_details=[
                ErrorDetails(
                    message="Os dados informados para o veículo já existem na base"
                ).to_dict()
            ],
        ),
    ]
)

BUSCAR_VEICULO_DEFAULT_RESPONSES = parse_openapi(
    [
        Message(
            status=400,
            error="Bad Request",
            message="Filtro inválido",
            error_details=[
                ErrorDetails(message="É preciso informar ao menos um filtro.").to_dict()
            ],
        ),
    ]
)

BUSCAR_UM_VEICULO_DEFAULT_RESPONSES = parse_openapi(
    [
        Message(
            status=404,
            error="Not found",
            message="Registro não encontrado",
            error_details=[
                ErrorDetails(
                    message="Não foi encontrado um registro a partir do id informado."
                ).to_dict()
            ],
        ),
    ]
)

ATUALIZAR_VEICULO_DEFAULT_RESPONSES = parse_openapi(
    [
        Message(
            status=404,
            error="Not found",
            message="Registro não encontrado",
            error_details=[
                ErrorDetails(
                    message="Não foi encontrado um registro a partir do id informado."
                ).to_dict()
            ],
        ),
        Message(
            status=400,
            error="Bad request",
            message="Atualização inválida",
            error_details=[
                ErrorDetails(
                    message="Não foram informados campos para a atualização do registro."
                ).to_dict()
            ],
        ),
    ]
)

DELETAR_VEICULO_DEFAULT_RESPONSES = parse_openapi(
    [
        Message(
            status=404,
            error="Not found",
            message="Registro não encontrado",
            error_details=[
                ErrorDetails(
                    message="Não foi encontrado um registro a partir do id informado."
                ).to_dict()
            ],
        ),
    ]
)