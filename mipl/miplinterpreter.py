import pathlib
import sys
from mipl.parser.parser import parser


class MIPLInterpreter:
    def __init__(self, file_path: str | pathlib.Path):
        self.file_name = file_path
        self.variables = {}
        self.functions = {}
        self.args = sys.argv[2:]

        self.token_tree: list[str] = []

    def parse(self) -> None:
        print('parse', self.file_name)
        with open(self.file_name, 'r') as f:
            data = f.read()
        self.token_tree = parser.parse(data)
        print(self.token_tree)

    def execute(self) -> None:
        print('execute', self.file_name)

    def start(self):
        print('start file', self.file_name)
        print(self.args)
        self.parse()
        self.execute()
