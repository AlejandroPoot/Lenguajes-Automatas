from antlr4 import *
from proyecto_finalLexer import proyecto_finalLexer
from proyecto_finalParser import proyecto_finalParser
from listenerProject import listenerProject

def main():
    # Solicitar al usuario el nombre del archivo de entrada
    input_file = input("Por favor, introduce el nombre del archivo de entrada (incluye la extensión): ")
    
    try:
        # Leer el archivo de entrada proporcionado
        with open(input_file, "r") as file:
            input_stream = InputStream(file.read())
        
        lexer = proyecto_finalLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = proyecto_finalParser(token_stream)
        tree = parser.programa()

        # Crear y usar el listener
        listener = listenerProject()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        # Solicitar el nombre del archivo de salida
        output_file = input("Por favor, introduce el nombre del archivo de salida (incluye la extensión .py): ")
        # Escribir la salida en el archivo
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(listener.output))
        
        print(f"Traducción completada. El código traducido se guardó en {output_file}")

    except FileNotFoundError:
        print(f"El archivo {input_file} no fue encontrado. Por favor, verifica el nombre y vuelve a intentarlo.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
