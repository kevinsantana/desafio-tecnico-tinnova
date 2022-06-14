import uvicorn

from cadastro_veiculos.app import start_application


def start():
    print(__package__, " started.")


if __name__ == "__main__":
    uvicorn.run(start_application(), host="127.0.0.1", port=7000, log_level="info")
