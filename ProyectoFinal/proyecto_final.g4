grammar proyecto_final;

// Delimiters
LPAREN      : '(' ;                  // (
RPAREN      : ')' ;                  // )
LBRACE      : '{' ;                  // {
RBRACE      : '}' ;                  // }
SEMI        : ';' ;                  // ;
COMMA       : ',' ;                  // ,

// Keywords (using geometric shapes)
DEF_FUNC     : 'circulo' ;            // Declaracion de funciones
RETURN    : 'cuadrado' ;           // Return de un resultado de la funcion
UNTIL   : 'triangulo' ;          // Valor que pertenece a un rango
RECTANGULO  : 'rectangulo' ;         // Limite de un bucle
TRUE   : 'pentagono' ;          // Boleano true
FALSE    : 'hexagono' ;           // Boleano false
PRINT   : 'heptagono' ;          // Impresion en pantalla

// Operators
PLUS        : '+' ;                  // Suma
MINUS       : '-' ;                  // Resta
MUL         : '*' ;                  // Multiplicacion
DIV         : '/' ;                  // Division
RAIZ        : 'raiz' ;               // Raiz
EQUAL   : 'octagono' ;           // Valores que son igual
NO_EQUAL    : 'nonagono' ;           // Valores que no son iguales
MAYOR    : 'decagono' ;           // Mayor que
MENOR   : 'icosaedro' ;          // Menor que
MAYOR_EQUAL  : 'dodecaedro' ;         // Mayor igual
MENOR_EQUAL : 'tetradecagono' ;    // Menor igual

// Variable Types
TEXT        : 'cubo' ;               // Texto o palabras
INTERGER    : 'esfera' ;             // Integer
DECIMAL    : 'cilindro' ;           // Decimal
BOOLEAN        : 'cono' ;               // Boolean

// Control Structures
IF_STRUCTURE    : 'trapecio' ;           // If
ELSE_STRUCTURE       : 'rombo' ;              // Else
FOR_STRUCTURE      : 'elipse' ;             // For loop
WHILE_STRUCTURE : 'paralelepipedo' ;  // While loop

// Literals
STRING      : '"' (~["\\] | '\\' .)* '"' ; // Strings
NUMBER      : [0-9]+ ('.' [0-9]+)? ;      // Integers or decimals

// Identifiers
ID          : [a-zA-Z_][a-zA-Z_0-9]* ;   // Variables or function names

// Whitespace and Comments
WS          : [ \t\r\n]+ -> skip ;        // Ignore whitespace
COMMENT     : '//' ~[\r\n]* -> skip ;     // Single-line comments



//Parse rules
programa: sentenceDeclare+;

// Declaración de variables
varDeclare
    : (TEXT | INTERGER | DECIMAL | BOOLEAN) ID EQUAL expresion SEMI
    ;

// Declaración de funciones
funcDeclare
    : DEF_FUNC ID LPAREN listaParam? RPAREN LBRACE sentenceDeclare* RBRACE
    ;

// Estructuras de control (IF-ELSE)
structureControl
    : IF_STRUCTURE LPAREN expresion RPAREN LBRACE sentenceDeclare* RBRACE 
      (ELSE_STRUCTURE LBRACE sentenceDeclare* RBRACE)?
    ;

// Bucles (FOR y WHILE)
ciclo
    : FOR_STRUCTURE (TEXT | INTERGER | DECIMAL | BOOLEAN) ID RECTANGULO expresion 
      (UNTIL expresion)? LBRACE sentenceDeclare* RBRACE
    | WHILE_STRUCTURE LPAREN expresion RPAREN LBRACE sentenceDeclare* RBRACE
    ;

// Sentencia PRINT
imprimirStatement
    : PRINT LPAREN expresion RPAREN SEMI
    ;

// Sentencia RETURN
returnStatement 
    : RETURN expresion SEMI
    ;

// Expresión general
expresionStatement 
    : expresion SEMI
    ;

// Parámetros de funciones
listaParam
    : (TEXT | INTERGER | DECIMAL | BOOLEAN) ID 
      (COMMA (TEXT | INTERGER | DECIMAL | BOOLEAN) ID)*
    ;

// Expresiones
expresion
    : expresion (PLUS | MINUS | MUL | DIV) expresion           // Operaciones aritméticas
    | expresion (MAYOR | MENOR | MAYOR_EQUAL | MENOR_EQUAL | NO_EQUAL | EQUAL) expresion // Operadores relacionales
    | RAIZ LPAREN expresion RPAREN                              // Raíz cuadrada
    | LPAREN expresion RPAREN                                   // Expresión entre paréntesis
    | STRING                                                     // Texto
    | NUMBER                                                     // Número
    | ID                                                        // Identificador
    | funcionLlamada
    ;

// Llamada a funciones
funcionLlamada
    : ID LPAREN listaArgument? RPAREN
    ;

// Argumentos de funciones
listaArgument
    : expresion (COMMA expresion)*
    ;

// Declaración de sentencias
sentenceDeclare
    : varDeclare
    | funcDeclare
    | structureControl
    | ciclo
    | imprimirStatement
    | returnStatement
    | expresionStatement
    ;