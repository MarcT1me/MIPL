start: (void_function | ret_function | variable_declaration | call_function | named_codeblock | codeblock)*

// отсутсвие данных
VOID: "void"
NULL: "null"

// целые числа
UINT8: "uint8"
UINT32: "uint32"
UINT: "uint" | UINT8 | UINT32

INT8: "int8"
INT32: "int32"
INT: "int" | INT8 | INT32 | UINT

// плавающие запятые
FLOAT: "float"
DOUBLE: "double"

// единственный возможный тип символов
CHAR: "char"

// векторы
VEC2: "vec2"
VEC3: "vec3"
VEC4: "vec4"
VEC: VEC2 | VEC3 | VEC4

// глобальные типы данных
NUM: INT | FLOAT | DOUBLE | NULL
VAR_TYPE: NUM | VEC | CHAR

// создание тип данных
NUMBER_DECLARATION: / \d+(\.\d+)? /
CHAR_DECLARATION: /"."/
VECTOR_DECLARATION: /"vec"[234] "(" value ("," value)* ")"/

// взаимодействия с числами
PLUS: "+"
MULTIPLE: "*"
DIVISION: "/"
MINUS: "-"
ARITHMETIC_SIGNS: PLUS | MINUS | MULTIPLE | DIVISION

// кеворды и символы
SEMICOLON: ";"
EQUAL: "=="
ASSIGNED: "="
NOT_EQUAL: "!="
NOT: "!"
IF: "if"
ELSE: "else"

// создания переменных
ID: /[a-zA-Z_][a-zA-Z0-9_]*/

// переменные
_value: ID | NUMBER_DECLARATION | CHAR_DECLARATION | VECTOR_DECLARATION
value: _value (ARITHMETIC_SIGNS _value)*
var: VAR_TYPE ID | VAR_TYPE ID "=" value
variable_declaration: VAR_TYPE ID SEMICOLON | VAR_TYPE ID ASSIGNED value SEMICOLON

// блоки кода
code_body: /[^{}]+/
codeblock: "{" code_body "}"
named_codeblock: ID codeblock SEMICOLON

// функции
func_args: var? ("," var)*
ret_function: VAR_TYPE ID "(" func_args ")" codeblock SEMICOLON
void_function: VOID ID "(" func_args ")" codeblock SEMICOLON

func_call_args: value? | value ("," value)*
call_function: ID "(" func_call_args ")" SEMICOLON

// игнорируемые символы
%import common.WS
%ignore WS

// комментарии
%ignore /\/\/.*/
%ignore /\/\*[\s\S]*?\*\//
