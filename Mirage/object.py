from typing import Any
from lark import Transformer, Token
from abc import abstractmethod


class MIPLObject:
    __type__ = 'Object'
    __transformer__: Transformer

    def __init__(self, ID, field, value=None):
        self.name: str = ID
        self.value: Any = value
        self.field = field
        self.tokens: list[Token] = []
        field[ID] = self

    def __o_construct__(self, tree) -> list[Token]:
        self.tokens = self.__transformer__.transform(tree)
        return self.tokens

    @abstractmethod
    def __o_free__(self) -> None: ...
