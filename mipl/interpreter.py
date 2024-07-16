import pathlib
import sys
from mipl.parser.parser import parser
from dataclasses import dataclass
from mipl.code.block import CodeBlock
from pprint import pprint


class MIPLInterpreter:
    @dataclass
    class Globals:
        __thunders__ = {}
        variables = {}
        functions = {}

    @dataclass
    class Locals:
        variables = {}
        functions = {}

    globals = Globals()

    args = sys.argv[2:]
    file_name: str | pathlib.Path
    token_tree = []

    def __new__(cls, file_path: str | pathlib.Path):
        cls.file_name = file_path
        return cls

    @classmethod
    def parse(cls) -> None:
        print('parse', cls.file_name)
        with open(cls.file_name, 'r') as f:
            data = f.read()
        code_block = CodeBlock()
        cls.token_tree = parser.parse(data)
        result = code_block.__o_construct__(cls.token_tree)
        print('result =', result)

    @classmethod
    def execute(cls) -> None:
        print('execute', cls.file_name)

    @classmethod
    def start(cls):
        print('start file', cls.file_name)
        print(cls.args)
        cls.parse()
        cls.execute()
