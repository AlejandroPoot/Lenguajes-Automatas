from antlr4 import *
from TraductorPyJavaParser import TraductorPyJavaParser
from TraductorPyJavaListener import TraductorPyJavaListener
import os

class ListenerOperacion(TraductorPyJavaListener):
    def __init__(self):
        self.codigo_java = []
        self.expresion_actual = ""
        
    def enterPrograma(self, ctx:TraductorPyJavaParser.ProgramaContext):
        self.codigo_java.append("public class Programa {")
        
    def exitPrograma(self, ctx:TraductorPyJavaParser.ProgramaContext):
        self.codigo_java.append("\n    public static void main(String[] args) {")
        self.codigo_java.append("        System.out.println(operations(5, 10, 3));")
        self.codigo_java.append("    }")
        self.codigo_java.append("}")
        
    def enterFuncion(self, ctx:TraductorPyJavaParser.FuncionContext):
        self.codigo_java.append("    public static int operations(")
        
    def enterParametros(self, ctx:TraductorPyJavaParser.ParametrosContext):
        params = []
        for id_token in ctx.ID():
            params.append("int " + id_token.getText())
        self.codigo_java.append(", ".join(params) + ") {")
        
    def enterAsignacion(self, ctx:TraductorPyJavaParser.AsignacionContext):
        self.expresion_actual = ""  
        
    def exitAsignacion(self, ctx:TraductorPyJavaParser.AsignacionContext):
        # Construimos la linea de asignación
        linea = f"        int {ctx.ID().getText()} = {self.expresion_actual};"
        self.codigo_java.append(linea)
        
    def enterExpresion(self, ctx:TraductorPyJavaParser.ExpresionContext):
        # Capturamos la expresión 
        self.expresion_actual = f"(({ctx.getText()}))"
        
    def exitCuerpo(self, ctx:TraductorPyJavaParser.CuerpoContext):
        self.codigo_java.append("        return op;")
        self.codigo_java.append("    }")
        
    def enterTermino(self, ctx:TraductorPyJavaParser.TerminoContext):
        pass
        
    def enterFactor(self, ctx:TraductorPyJavaParser.FactorContext):
        pass
        
    def get_codigo_java(self):
        return "\n".join(self.codigo_java)
    
    def guardar_archivo(self, ruta_salida="TraductorPyJava"):
        ruta_archivo = os.path.join(ruta_salida, "Programa.java")
        try:
            with open(ruta_archivo, "w") as archivo:
                archivo.write(self.get_codigo_java())
            print(f"Archivo Java generado exitosamente en: {ruta_archivo}")
        except Exception as e:
            print(f"Error al guardar el archivo: {str(e)}")