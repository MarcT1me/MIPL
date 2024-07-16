from lark import Lark, Transformer, v_args

# Определение грамматики
with open('mipl/parser/grammar') as file:
    grammar = file.read()
# Создание парсера
parser = Lark(grammar, parser='lalr')


class FuncArgsTransformer(Transformer):
    def var(self, arg):
        type, name = arg
        return {
            'type': type.value,
            'name': name.value,
        }


# Трансформер для извлечения данных
@v_args(inline=True)
class FunctionTransformer(Transformer):
    def void_function(self, type, name, args, body, _):
        return {
            'f_type': 'void',
            'f_name': name.value,
            'f_args': args,
            'f_body': body.value
        }

    def ret_function(self, type, name, args, body, _):
        return {
            'f_type': type.value,
            'f_name': name.value,
            'f_args': args,
            'f_body': body.value
        }

    def TYPE(self, token):
        print(token)
        return token

    def ID(self, token):
        return token

    def func_args(self, *trees):
        return [FuncArgsTransformer().transform(tree) for tree in trees]

    def func_body(self, token):
        return token
