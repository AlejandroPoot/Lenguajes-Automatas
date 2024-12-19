from proyecto_finalListener import proyecto_finalListener
from proyecto_finalParser import proyecto_finalParser
import math

class listenerProject(proyecto_finalListener):
    def __init__(self):
        self.output = []  # List to store generated lines of code
        self.indent_level = 0  # Indentation level

    def indent(self):
        """Returns the current indentation."""
        return "    " * self.indent_level

    def write(self, line):
        """Adds a line with the current indentation."""
        self.output.append(f"{self.indent()}{line}")

    # Variable Declaration
    def exitVarDeclare(self, ctx: proyecto_finalParser.VarDeclareContext):
        tipo = ctx.getChild(0).getText()
        variable = ctx.ID().getText()
        valor = ctx.expresion().getText()

        # Replace operators in the value
        valor = (
            valor.replace('raiz', 'math.sqrt')
            .replace('octagono', '=')  # Changed to single = for assignment
            .replace('decagono', '<')
            .replace('icosaedro', '>')
            .replace('nonagono', '!=')
        )

        # Translate types
        tipo_python = {
            "cubo": "str",
            "esfera": "int",
            "cilindro": "float",
            "cono": "bool"
        }.get(tipo, "unknown")

        self.write(f"# Declaracion: {tipo_python} {variable} = {valor}")
        self.write(f"{variable} = {valor}")

    # Function Declaration
    def enterFuncDeclare(self, ctx: proyecto_finalParser.FuncDeclareContext):
        nombre = ctx.ID().getText()
        parametros = []

        if ctx.listaParam():
            for param in ctx.listaParam().getChildren():
                if param.getText() != ',':
                    parametros.append(param.getText())

        # Remove duplicate parameters
        parametros = list(dict.fromkeys(parametros))
        parametros_str = ", ".join(parametros)

        self.write(f"def {nombre}({parametros_str}):")
        self.indent_level += 1

    def exitFuncDeclare(self, ctx: proyecto_finalParser.FuncDeclareContext):
        self.indent_level -= 1
        self.write("")  # Blank line to separate functions

    # If-Else Structure
    def enterStructureControl(self, ctx: proyecto_finalParser.StructureControlContext):
        # Handle custom operators
        condicion = "True"
        if ctx.expresion():
            condicion = ctx.expresion().getText()
            condicion = (
                condicion.replace("decagono", "<")
                .replace("icosaedro", ">")
                .replace("octagono", "==")
                .replace("dodecaedro", ">=")
                .replace("tetradecagono", "<=")
            )

        self.write(f"if {condicion}:")
        self.indent_level += 1

    def exitStructureControl(self, ctx: proyecto_finalParser.StructureControlContext):
        self.indent_level -= 1  # End 'if' block

        # If there is an 'else' block
        if ctx.ELSE_STRUCTURE():
            self.write("else:")  # Write 'else:' with the correct indentation
            self.indent_level += 1  # Increase indentation for the 'else' block

            # Process statements within the 'else' block
            for sentencia in ctx.sentenceDeclare():
                if isinstance(sentencia, proyecto_finalParser.ImprimirStatementContext):
                    texto = sentencia.expresion().getText()
                    self.write(f"print({texto})")
            self.indent_level -= 1

    # Print Statement
    def exitImprimirStatement(self, ctx: proyecto_finalParser.ImprimirStatementContext):
        texto = ctx.expresion().getText()
        print(texto.strip('"'))
        self.write(f"print({texto})")

    def exitExpresionStatement(self, ctx: proyecto_finalParser.ExpresionStatementContext):
        if ctx.expresion():
            # Si ctx.expresion() es una lista de expresiones, manejarlas adecuadamente
            expresion = ""
            
            # Si ctx.expresion() es un solo nodo, obtén el texto directamente
            if isinstance(ctx.expresion(), list):
                expresion = " ".join([e.getText() for e in ctx.expresion()])  # Unimos el texto de la lista
            else:
                expresion = ctx.expresion().getText()  # Solo obtenemos el texto del único nodo
            
            # Realizamos las sustituciones de operadores
            expresion = (
                expresion.replace("decagono", "<")
                .replace("icosaedro", ">")
                .replace("octagono", "=")
                .replace("nonagono", "!=")
                .replace("raiz", "math.sqrt")  # Si es una función, la manejamos aquí
            )
            self.write(expresion)

    def enterCiclo(self, ctx: proyecto_finalParser.CicloContext):
        if ctx.FOR_STRUCTURE():
            variable = ctx.ID().getText()
            inicio = ctx.expresion(0).getText()
            fin = ctx.expresion(1).getText()
            self.write(f"for {variable} in range({inicio}, {fin}):")
            self.indent_level += 1
        elif ctx.WHILE_STRUCTURE():
            # Check that the condition is not null
            if ctx.expresion():
                # Get the expression text safely
                condicion = ""
                expr = ctx.expresion()
                if hasattr(expr, 'getText'):
                    condicion = expr.getText()
                elif isinstance(expr, list):
                    condicion = " ".join([e.getText() for e in expr if hasattr(e, 'getText')])
                else:
                    condicion = str(expr)
                    
                # Translate custom operators
                condicion = (
                    condicion.replace("decagono", ">")
                    .replace("icosaedro", "<")
                    .replace("octagono", "=")
                    .replace("nonagono", "!=")
                )
                self.write(f"while {condicion}:")
                self.indent_level += 1

    def exitCiclo(self, ctx: proyecto_finalParser.CicloContext):
        self.indent_level -= 1

    # Return Statement
    def exitReturnStatement(self, ctx: proyecto_finalParser.ReturnStatementContext):
        valor = ctx.expresion().getText()
        self.write(f"return {valor}")

    def exitExpresion(self, ctx):
        # Si la expresión es binaria (con operadores)
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0)
            operator = ctx.getChild(1)
            right = ctx.getChild(2)

            # Procesar los operandos
            left_text = left.getText() if hasattr(left, 'getText') else str(left)
            right_text = right.getText() if hasattr(right, 'getText') else str(right)
            operator_text = operator.getText() if hasattr(operator, 'getText') else str(operator)

            # Reemplazar operadores personalizados con operadores estándar
            operator_map = {
                "octagono": "=",
                "decagono": ">",
                "icosaedro": "<",
                "nonagono": "!=",
                "dodecaedro": ">=",
                "tetradecagono": "<=",
                "raiz": "math.sqrt"
            }

            # Si el operador es uno de los operadores personalizados, reemplázalo
            operator_final = operator_map.get(operator_text, operator_text)

            # Manejar específicamente la función raiz
            if operator_text == "raiz":
                return f"math.sqrt({right_text})"
            
            # Devuelve la expresión con el operador reemplazado
            return f"{left_text} {operator_final} {right_text}"

        # Si la expresión es de tipo 'raiz', maneja específicamente esta operación
        elif ctx.RAIZ():
            expr = ctx.expresion()
            expr_text = expr.getText() if hasattr(expr, 'getText') else str(expr)
            return f"math.sqrt({expr_text})"

        # Si es una expresión entre paréntesis, maneja esto también
        elif ctx.LPAREN():
            expr = ctx.expresion()
            expr_text = expr.getText() if hasattr(expr, 'getText') else str(expr)
            return f"({expr_text})"
        
        # Si no es una expresión compleja, simplemente retorna el texto tal cual
        text = ctx.getText() if hasattr(ctx, 'getText') else str(ctx)
        # Realizar reemplazo final por si acaso
        if text.startswith('raiz('):
            return text.replace('raiz', 'math.sqrt')
        return text
