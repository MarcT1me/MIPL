from mipl.object import MIPLObject
from lark import Transformer, v_args, Token, Tree


class Argument(MIPLObject):
    __type__ = 'function_argument'

    @v_args(inline=True)
    class ATransformer(Transformer):
        def var(self, type: Token, name: Token):
            return {
                'type': type.value,
                'name': name.value,
            }

    __transformer__ = ATransformer()

    def __init__(self, ID, field, a_var):
        super().__init__(ID, field, value=a_var)
        self.default = a_var.valuse

    def __o_free__(self) -> None: del self.field.variables[self.name]


class Function(MIPLObject):
    __type__ = 'function'

    @v_args(inline=True)
    class FTransformer(Transformer):
        def void_function(self, type: Token, name: Token, args: list[Token], body: Token, _) -> dict:
            return {
                'f_type': 'void',
                'f_name': name.value,
                'f_args': args,
                'f_body': body.value
            }

        def ret_function(self, type: Token, name: Token, args: Token, body: Token, _) -> dict:
            return {
                'f_type': type.value,
                'f_name': name.value,
                'f_args': args,
                'f_body': body.value
            }

        def func_args(self, *trees: Tree) -> list[Token]:
            return [Argument.ATransformer().transform(tree) for tree in trees]

    __transformer__ = FTransformer()

    def __init__(self, ID, field, f_type: str, f_args: list[Argument]):
        super().__init__(ID, field)
        self.ret_type = f_type
        self.args = f_args

    def __f_call__(self, *args):
        assert len(args) == len(self.args)
        for arg_i in range(len(args)):
            self.args[arg_i].value = args[arg_i]
        ...

    def __o_free__(self) -> None: del self.field.functions[self.name]
