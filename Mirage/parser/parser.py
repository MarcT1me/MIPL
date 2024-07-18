import os.path
from lark import Lark, Transformer, v_args, Token, Tree, LarkError, exceptions

grammar_categories = (
    'base', 'codeblock',
    'types', 'specials', 'values',
    # 'conditions', 'functions'
    # 'structs', 'classes'
)
# grammar_categories.clear()
#
# with open('Mirage/parser/grammar.lark') as f:
#     grammar += f.read()

grammar = ""

for category in grammar_categories:
    path = rf'Mirage/parser/grammar/{category}.lark'
    if os.path.exists(path):
        with open(path) as file:
            data = file.readlines()
        for line in data:
            if any(f'%import {category}.lark' in line for category in grammar_categories):
                continue
            grammar += f'{line}\n'

parser: Lark = ...


def parse_grammar():
    global parser
    print(grammar)
    try:
        parser = Lark(grammar, parser='lalr')
    except Exception as le:
        if isinstance(le, exceptions.UnexpectedCharacters):
            print(f"Ошибка лексера: Неожиданный символ '{vars(le)}'.")
        elif isinstance(le, exceptions.UnexpectedToken):
            print(f"Ошибка лексера: Невалидный токен '{vars(le)}'.")
        else:
            raise le


@v_args(inline=True)
class GrammarTransformerMain(Transformer):
    def VAR_TYPE(self, token: Token):
        return token

    def ID(self, token: Token):
        return token

    def code_body(self, token: Token):
        return token

