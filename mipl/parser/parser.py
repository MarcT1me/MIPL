from lark import Lark, Transformer, v_args, Token, Tree

with open('mipl/parser/grammar.g') as file:
    grammar = file.read()

parser = Lark(grammar, parser='lalr')


@v_args(inline=True)
class GrammarTransformerMain(Transformer):
    def VAR_TYPE(self, token: Token):
        return token

    def ID(self, token: Token):
        return token

    def code_body(self, token: Token):
        return token

