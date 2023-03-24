import datetime
from typing import List
from Usuario import Usuario
from Produto import Produto

class Movimentacao:
    def __init__(self, id_movimentacao: int, data_movimentacao: str, usuario: Usuario, produto: Produto, qtd_produto: int):
        self.__id_movimentacao = id_movimentacao
        self.__data_movimentacao = datetime.datetime.strptime(data_movimentacao, '%Y-%m-%d').date()
        self.__usuario = usuario
        self.__produto = produto
        self.__qtd_produto = qtd_produto

    @property
    def id_movimentacao(self) -> int:
        return self.__id_movimentacao

    @property
    def data_movimentacao(self) -> str:
        return self.__data_movimentacao.strftime('%Y-%m-%d')

    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def produto(self) -> Produto:
        return self.__produto

    @property
    def qtd_produto(self) -> int:
        return self.__qtd_produto

    @staticmethod
    def from_dict(movimentacao_dict: dict) -> 'Movimentacao':
        return Movimentacao(
            movimentacao_dict['id_movimentacao'],
            movimentacao_dict['data_movimentacao'],
            Usuario.from_dict(movimentacao_dict['usuario']),
            Produto.from_dict(movimentacao_dict['produto']),
            movimentacao_dict['qtd_produto']
        )

    @staticmethod
    def to_dict(movimentacao: 'Movimentacao') -> dict:
        return {
            'id_movimentacao': movimentacao.id_movimentacao,
            'data_movimentacao': movimentacao.data_movimentacao,
            'usuario': Usuario.to_dict(movimentacao.usuario),
            'produto': Produto.to_dict(movimentacao.produto),
            'qtd_produto': movimentacao.qtd_produto
        }

    @staticmethod
    def from_list(movimentacao_list: List[dict]) -> List['Movimentacao']:
        return [Movimentacao.from_dict(mov_dict) for mov_dict in movimentacao_list]

    @staticmethod
    def to_list(movimentacao: List['Movimentacao']) -> List[dict]:
        return [Movimentacao.to_dict(mov) for mov in movimentacao]
