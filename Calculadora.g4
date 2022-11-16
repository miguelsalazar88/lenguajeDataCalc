grammar Calculadora;

parse
: from_input
| from_file
;

from_input
: stat NEWLINE
;

from_file
: (stat | NEWLINE)* EOF
;

stat
: simple_stat
| compound_stat 
;

compound_stat
: for_stat
| while_stat
;

simple_stat
: assignment
| imprimir
| importar
| retornar
| expr
| atom NEWLINE
| range
| matrices
| OTHER
;

matrices
: matmul
| matsum
| matrest
| transpose
| inverse
;

inverse
: INVERSE OPAR atom CPAR
;

matmul
: MATMUL OPAR atom COMMA atom CPAR
;

matsum
: MATSUM OPAR atom COMMA atom CPAR
;

matrest
: MATREST OPAR atom COMMA atom CPAR
;

transpose
: TRANSPOSE OPAR atom CPAR
;

for_stat
: FOR (SPACE)* ID (SPACE)* IN (SPACE)* (variable|array|range) (SPACE)* stat_block
;

while_stat
: WHILE (SPACE)* OPAR expr CPAR (SPACE)* stat_block
;

range
: RANGE OPAR (INT| INT COMMA INT) CPAR
;

stat_block
: OBRACE (stat|NEWLINE)* CBRACE
| stat NEWLINE
;

assignment
: variable ASSIGN (assignment|expr)
;

importar
: IMPORT ID (POINT ID)*
| FROM ID IMPORT ID
;

retornar
: RETURN OPAR expr CPAR NEWLINE
;

expr
: <assoc=right>left=expr POW right=expr        #powExpr
| MINUS expr                                   #unaryMinusExpr
| NOT (SPACE)* expr                            #notExpr
| left=expr op=(MULT|DIV|MOD) right=expr       #multiplicationExpr
| left=expr op=(PLUS|MINUS) right=expr         #additiveExpr
| left=expr op=(LTEQ|GTEQ|LT|GT) right=expr    #relationalExpr
| left=expr op=(EQ|NEQ) right=expr             #equalityExpr
| left=expr AND right=expr                     #andExpr
| left=expr OR right=expr                      #orExpr
| OPAR expr CPAR 						       #parExpr
| trigo                                        #trigoExpr
| raiz                                         #sqrtExpr
| plot                                         #plotExpr
| atom                                         #atomExpr
;


atom 
: (INT|FLOAT)  #numberAtom
| (TRUE|FALSE) #booleanAtom
| STRING       #stringAtom
| array		#arrayAtom
| accessarray  #accessToarray
| variable		#accessVariable
| SPACE         #spaceAtom
| NONE         #noneAtom 
;

array
: OKEY (expr (COMMA expr)*)? CKEY
| OKEY (array(COMMA array)*) CKEY
;

accessarray
: variable OKEY expr CKEY
;

variable
: ID (POINT ID)* (OPAR(expr (COMMA expr)*)? CPAR)?
| ID (POINT ID)* OKEY expr CKEY
;

parametro
: ID (ASSIGN expr)?
;

trigo
: (SIN|COS|TAN|ASIN|ACOS|ATAN) OPAR expr CPAR
;

raiz
: SQRT OPAR expr CPAR
;

imprimir
: PRINT OPAR expr CPAR
;

plot
: PLOT OPAR atom (COMMA atom)* CPAR
;

MATMUL : 'matmul';
TRANSPOSE : 'transpose';
MATSUM : 'matsum';
MATREST : 'matrest';
INVERSE : 'inverse';


SQRT : 'sqrt';

SIN : 'sin';
COS : 'cos';
TAN : 'tan';
ASIN: 'asin';
ACOS: 'acos';
ATAN: 'atan';

OR: 'or';
AND : 'and';
EQ : '==';
NEQ : '!=';
GT : '>';
LT : '<';
GTEQ : '>=';
LTEQ : '<=';
PLUS : '+';
MINUS : '-';
MULT : '*';
DIV : '/';
MOD : '%';
POW : '**';
NOT : 'not';

ASSIGN : '=';
OPAR : '(';
CPAR : ')';
OBRACE : '{';
CBRACE : '}';
OKEY : '[';
CKEY : ']';
COMMA : ',';
SEMICOLON : ';';
COLON : ':';

RANGE: 'range';
PLOT : 'plot';
TRUE : 'True';
FALSE : 'False';
NONE : 'None';
IF : 'if';
ELSE : 'else';
WHILE : 'while';
PRINT : 'print';
FOR : 'for';
IN: 'in';
FUNCTION : 'def';  
END : 'end';
RETURN : 'return';
IMPORT : 'import';
FROM : 'from';
ASTERISC: 'todo';
POINT : '.';



ID : [a-zA-Z_] [a-zA-Z_0-9]*;
INT : [0-9]+;
FLOAT : [0-9]+ '.' [0-9]* | '.'[0-9]+;
STRING : '"' (~["\r\n] | '""')* '"';
COMMENT : '#' ~[\r\n]* -> skip;
SPACE : ' ';
NEWLINE : [\n];
OTHER : . ;