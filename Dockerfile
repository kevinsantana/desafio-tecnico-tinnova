FROM ubuntu:22.04

# DEPENDENCIES
RUN apt-get update \
    apt-get install python3.10.04 -y \
    apt-get install python3-pip -y \
    apt-get install -y python-dev \
    apt install libpq-dev
RUN pip install --upgrade pip
RUN apt-get clean

# INSTALL APPLICATION
COPY ./cadastro_veiculos /deploy/cadastro_veiculos
COPY ./docs /deploy/docs
COPY setup.py /deploy
COPY /tests /deploy/tests
COPY README.md /deploy

WORKDIR /deploy

RUN pip install -e . 

EXPOSE 7000