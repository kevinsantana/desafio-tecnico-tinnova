from cadastro_veiculos.excecoes import CadastroVeiculosException


class MarcaNaoExisteException(CadastroVeiculosException):
    def __init__(
        self,
        status: int,
        error: str,
        message: str,
        error_details: list = [],
    ):
        self.status = status
        self.error = error
        self.message = message
        self.error_details = error_details
        super().__init__(status, error, message, error_details)


class FiltroInvalidoException(CadastroVeiculosException):
    def __init__(
        self,
        status: int,
        error: str,
        message: str,
        error_details: list = [],
    ):
        self.status = status
        self.error = error
        self.message = message
        self.error_details = error_details
        super().__init__(status, error, message, error_details)


class VeiculoNaoEncontradoException(CadastroVeiculosException):
    def __init__(
        self,
        status: int,
        error: str,
        message: str,
        error_details: list = [],
    ):
        self.status = status
        self.error = error
        self.message = message
        self.error_details = error_details
        super().__init__(status, error, message, error_details)


class AtualizacaoInvalidaException(CadastroVeiculosException):
    def __init__(
        self,
        status: int,
        error: str,
        message: str,
        error_details: list = [],
    ):
        self.status = status
        self.error = error
        self.message = message
        self.error_details = error_details
        super().__init__(status, error, message, error_details)
