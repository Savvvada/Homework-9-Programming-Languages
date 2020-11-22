import ply.yacc as yacc
from MiniCLexer import tokens




def p_waeStart(p):
    'waeStart : wae SEMI'
    p[0] = p[1]

def p_waeStart2(p):
    'waeStart : wae SEMI wae SEMI SEMI'
    p[0] = p[1] + p[3]


def p_waeStart3(p):
    'waeStart : wae SEMI wae SEMI'
    p[0] = p[1] + p[3]



def p_wae_1(p):
    'wae : NUMBER'
    p[0] = ['num',p[1]]

def p_wae_2(p):
    'wae : ID'
    p[0] = ['id',p[1]]

def p_optr_1(p):
  'wae : wae MINUS wae'
  p[0] = [p[1], 'optr', p[2], p[3]]


def p_optr_2(p):
  'wae : wae PLUS wae'
  p[0] = [p[1], 'optr', p[2], p[3]]


def p_optr_3(p):
  'wae : wae DIVIDE wae'
  p[0] = [p[1], 'optr', p[2], p[3]]


def p_optr_4(p):
  'wae : wae TIMES wae'
  p[0] = [p[1], 'optr', p[2], p[3]]

def p_optr_5(p):
  'wae : wae LESS wae'
  p[0] = [p[1], 'optr', p[2], p[3]]

def p_optr_6(p):
  'wae : wae GREATER wae'
  p[0] = [p[1]]+['optr', p[2]] + [p[3]]

def p_optr_7(p):
  'wae : wae LESSOREQUAL wae'
  p[0] = [p[1], 'optr', p[2], p[3]]

def p_optr_8(p):
  'wae : wae GREATEROREQUAL wae'
  p[0] = [p[1], 'optr', p[2], p[3]]

def p_optr_10(p):
  'wae : wae ISEQUAL wae'
  p[0] = [p[1], 'optr', p[2], p[3]]

def p_optr_11(p):
  'wae : wae EQUALS wae'
  p[0] = [p[1], 'optr', p[2], p[3]]

def p_wae_20(p):
  'wae : NOT wae'
  p[0] = ['optr', p[1], P[2]]

def p_loop_1(p):
  'wae : IF wae'
  p[0] = ['if', p[2]]

def p_loop_01(p):
  'wae : IF wae wae'
  p[0] = ['if', p[2], p[3]]


def p_loop_2(p):
  'wae : WHILE wae'
  p[0] = ['while', p[2]]

def p_waeloop(p):
  'wae : LBRACE wae RBRACE'
  p[0] = [p[2]]

def p_waeloop2(p):
  'wae : LPARA wae RPARA'
  p[0] = [p[2]]

def p_waeLoop4(p):
  'wae : wae wae wae'
  p[0] = p[1] + p[2] + p[3]





def p_error(p):
  print("Syntax error in input!")

def p_alist_01(p):
  'alist : LPARA ID wae RPARA'
  p[0] = [[p[2],p[3]]]

def p_alist_02(p):
  'alist : LPARA ID wae RPARA alist'
  p[0] = [[p[2],p[3]]] + p[5]

parser = yacc.yacc()