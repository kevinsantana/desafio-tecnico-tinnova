from fastapi import APIRouter

from cadastro_veiculos.rotas.v1 import healthcheck, veiculos


v1 = APIRouter()

v1.include_router(healthcheck.router, prefix="/health", tags=["healthcheck"])
v1.include_router(veiculos.router, prefix="/veiculos", tags=["veiculos"])
