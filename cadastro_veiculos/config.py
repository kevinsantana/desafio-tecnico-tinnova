import os
from enum import Enum
from typing import Any, Dict, Optional

from pydantic import BaseModel, BaseSettings, PostgresDsn, validator


class EnvironmentEnum(Enum):
    LOCAL = "LOCAL"
    PROD = "PROD"


class DatabaseModel(BaseModel):
    DATABASE_USER: str = "cadastro_veiculos"
    DATABASE_PASS: str = "cadastro_veiculos"
    DATABASE_HOST: str = "db_cadastro_veiculos"
    DATABASE_PORT: str = "5432"
    DATABASE_NAME: str = "cadastro_veiculos"
    DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

    @validator("DATABASE_URL", pre=True)
    def make_db_url(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        return PostgresDsn.build(
            scheme="postgresql",
            user=values["DATABASE_USER"],
            password=values["DATABASE_PASS"],
            host=values["DATABASE_HOST"],
            port=values["DATABASE_PORT"],
            path=f"/{values['DATABASE_NAME']}",
        )


class Envs(BaseSettings):
    ENVIRONMENT: Optional[Enum] = EnvironmentEnum.PROD
    DB_URI: str = DatabaseModel().DATABASE_URL
    MARCAS: str = os.environ.get("MARCAS", None)

    class Config:
        case_sensitive = True


envs = Envs()
