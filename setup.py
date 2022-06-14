# Source: https://packaging.python.org/guides/distributing-packages-using-setuptools/

from os import path
from cadastro_veiculos import __version__
from setuptools import find_packages, setup

run_requirements = [
    "loguru==0.6.0",
    "pydantic==1.9.1",
    "fastapi==0.78.0",
    "uvloop==0.16.0",
    "uvicorn==0.17.6",
    "gunicorn==20.1.0",
    "aiofiles==0.8.0",
    "requests==2.27.1",
    "sphinx-rtd-theme==1.0.0",
    "recommonmark==0.7.1",
    "Jinja2==3.1.2",
    "Sphinx==4.5.0",
    "starlette==0.19.1",
    "pytest==7.1.2",
    "sphinx-autobuild==2021.3.14",
    "psycopg2==2.9.3",
]

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="Cadastro Veiculos Api",
    version=__version__,
    author="Kevin de Santana Araujo",
    author_email="kevin_santana.araujo@hotmail.com",
    packages=find_packages(exclude=["docs", "tests"]),
    url="https://github.com/kevinsantana/desafio-tecnico-tinnova",
    description="API para manter o cadastro de veículos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=run_requirements,
    python_requires=">=3.10.4",
)
