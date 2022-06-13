from pydantic import BaseModel, Field

from cadastro_veiculos.excecoes import ErrorDetails
from cadastro_veiculos.models import parse_openapi, Message


class CriarVeiculoRequest(BaseModel):
    veiculo: str = Field(
        "Civic",
        description="Nome do veículo",
    )
    marca: str = Field("Honda", description="Marca do veículo")
    ano: int = Field(2022, description="Ano do veículo")
    descricao: str = Field(
        "Sedan esportivo", description="Uma descrição sobre o veículo"
    )
    vendido: bool = Field(False, description="Indicar se o veículo foi ou não vendido")


class CriarVeiculoResponse(BaseModel):
    id: int


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
