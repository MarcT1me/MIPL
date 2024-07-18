from Mirage.object import MIPLObject
from Mirage.parser.parser import GrammarTransformerMain, v_args, Token


class CodeBlock(MIPLObject):
    __type__ = 'codeblock'

    @v_args(inline=True)
    class CBTransformer(GrammarTransformerMain):
        def named_codeblock(self, name: Token, body: Token, _):
            return {
                'c_name': name.value,
                'c_body': body
            }

        def codeblock(self, body: Token):
            return {
                'c_body': body.value
            }

    __transformer__ = CBTransformer()

    def __init__(self): pass

    def __o_free__(self) -> None: pass
