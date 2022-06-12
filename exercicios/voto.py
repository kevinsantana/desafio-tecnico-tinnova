from dataclasses import dataclass


@dataclass
class Eleicao:
    """Contabiliza votos de uma eleicao"""

    total_eleitores: int
    validos: int
    brancos: int
    nulos: int

    def votos_validos(self) -> float:
        return (self.validos / self.total_eleitores) * 100

    def votos_branco(self) -> float:
        return (self.brancos / self.total_eleitores) * 100

    def votos_nulos(self) -> float:
        return (self.nulos / self.total_eleitores) * 100


if __name__ == "__main__":
    eleicao = Eleicao(total_eleitores=1000, validos=800, brancos=150, nulos=50)
    print(eleicao.votos_validos())
    print(eleicao.votos_branco())
    print(eleicao.votos_nulos())
