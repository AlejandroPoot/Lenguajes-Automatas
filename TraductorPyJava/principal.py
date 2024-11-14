from antlr4 import *
from TraductorPyJavaLexer import TraductorPyJavaLexer
from TraductorPyJavaParser import TraductorPyJavaParser
from ListenerOperacion import ListenerOperacion

# ... (resto del código igual)

def main():
    try:
        input_stream = FileStream("TraductorPyJava/proprueba.txt")
        
        lexer = TraductorPyJavaLexer(input_stream)
        
        stream = CommonTokenStream(lexer)
        
        parser = TraductorPyJavaParser(stream)
        
        tree = parser.programa()
        
        listener = ListenerOperacion()
        
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        
        listener.guardar_archivo()
        
        print("Código Java generado:")
        print(listener.get_codigo_java())
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()