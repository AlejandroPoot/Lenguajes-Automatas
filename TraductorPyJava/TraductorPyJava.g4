grammar TraductorPyJava;

// Reglas del parser
programa: funcion EOF;

funcion
    : 'def' ID '(' parametros ')' ':' 
      cuerpo
    ;

parametros
    : ID (',' ID)*
    ;

cuerpo
    : asignacion
      'return' expresion
    ;

asignacion
    : ID '=' expresion
    ;

expresion
    : termino (('+' | '-') termino)*
    ;

termino
    : factor (('*' | '/') factor)*
    ;

factor
    : ID
    | NUMERO
    | '(' expresion ')'
    ;

// Reglas del lexer
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMERO: [0-9]+;
WS: [ \t\r\n]+ -> skip;