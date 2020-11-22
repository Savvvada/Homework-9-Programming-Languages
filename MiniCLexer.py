import ply.lex as lex

reserved = { 'with': 'WITH', 'if': 'IF' }

tokens = ['NUMBER', 'ID', 'SEMI', 'LPARA', 'RPARA', 'WHILE', 'LBRACE', 'RBRACE', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'NOT', 'NOTEQUAL', 'ISEQUAL', 'AND', 'OR', 'LESS', 'GREATER', 'LESSOREQUAL', 'GREATEROREQUAL'] + list(reserved.values())

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPARA = r'\('
t_RPARA = r'\)'
t_WHILE = r'[wW][hH][iI][lL][eE]'
t_IF = r'[iI][fF]'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_NOT = r'!'
t_NOTEQUAL = r'!='
t_ISEQUAL = r'=='
t_AND = r'&&'
t_OR = r'\|\|'
t_LESS = r'<'
t_GREATER = r'>'
t_LESSOREQUAL = r'<='
t_GREATEROREQUAL = r'>='
t_SEMI = r';'

def t_NUMBER(t):
    r'[-+]?[0-9]+(\.([0-9]+)?)?'
    t.value = float(t.value)
    t.type = 'NUMBER'
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t

t_ignore = " \r\n\t"
t_ignore_COMMENT = r'\#.*'

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)
  raise Exception('LEXER ERROR')

lexer = lex.lex()

