from typing import List

class Produto:
    def __init__(self, id_produto: int, nome_produto: str, valor_produto: int, qtd_produto: int):
        self.__id_produto = id_produto
        self.__nome_produto = nome_produto
        self.__valor_produto = valor_produto
        self.__qtd_produto = qtd_produto

    @property
    def id_produto(self) -> int:
        return self.__id_produto

    @property
    def nome_produto(self) -> str:
        return self.__nome_produto

    @property
    def valor_produto(self) -> int:
        return self.__valor_produto

    @property
    def qtd_produto(self) -> int:
        return self.__qtd_produto

    @staticmethod
    def from_dict(produto_dict: dict) -> 'Produto':
        return Produto(
            produto_dict['id_produto'],
            produto_dict['nome_produto'],
            produto_dict['valor_produto'],
            produto_dict['qtd_produto']
        )

    @staticmethod
    def to_dict(produto: 'Produto') -> dict:
        return {
            'id_produto': produto.id_produto,
            'nome_produto': produto.nome_produto,
            'valor_produto': produto.valor_produto,
            'qtd_produto': produto.qtd_produto
        }

    @staticmethod
    def from_list(produto_list: List[dict]) -> List['Produto']:
        return [Produto.from_dict(prod_dict) for prod_dict in produto_list]

    @staticmethod
    def to_list(produto: List['Produto']) -> List[dict]:
        return [Produto.to_dict(prod) for prod in produto]
