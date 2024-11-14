# Generated from ./TraductorPyJava.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,68,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,
        2,5,2,31,8,2,10,2,12,2,34,9,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,
        5,1,5,1,5,5,5,47,8,5,10,5,12,5,50,9,5,1,6,1,6,1,6,5,6,55,8,6,10,
        6,12,6,58,9,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,66,8,7,1,7,0,0,8,0,2,4,
        6,8,10,12,14,0,2,1,0,8,9,1,0,10,11,64,0,16,1,0,0,0,2,19,1,0,0,0,
        4,27,1,0,0,0,6,35,1,0,0,0,8,39,1,0,0,0,10,43,1,0,0,0,12,51,1,0,0,
        0,14,65,1,0,0,0,16,17,3,2,1,0,17,18,5,0,0,1,18,1,1,0,0,0,19,20,5,
        1,0,0,20,21,5,12,0,0,21,22,5,2,0,0,22,23,3,4,2,0,23,24,5,3,0,0,24,
        25,5,4,0,0,25,26,3,6,3,0,26,3,1,0,0,0,27,32,5,12,0,0,28,29,5,5,0,
        0,29,31,5,12,0,0,30,28,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,
        1,0,0,0,33,5,1,0,0,0,34,32,1,0,0,0,35,36,3,8,4,0,36,37,5,6,0,0,37,
        38,3,10,5,0,38,7,1,0,0,0,39,40,5,12,0,0,40,41,5,7,0,0,41,42,3,10,
        5,0,42,9,1,0,0,0,43,48,3,12,6,0,44,45,7,0,0,0,45,47,3,12,6,0,46,
        44,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,11,1,0,0,
        0,50,48,1,0,0,0,51,56,3,14,7,0,52,53,7,1,0,0,53,55,3,14,7,0,54,52,
        1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,13,1,0,0,0,
        58,56,1,0,0,0,59,66,5,12,0,0,60,66,5,13,0,0,61,62,5,2,0,0,62,63,
        3,10,5,0,63,64,5,3,0,0,64,66,1,0,0,0,65,59,1,0,0,0,65,60,1,0,0,0,
        65,61,1,0,0,0,66,15,1,0,0,0,4,32,48,56,65
    ]

class TraductorPyJavaParser ( Parser ):

    grammarFileName = "TraductorPyJava.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'('", "')'", "':'", "','", "'return'", 
                     "'='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NUMERO", "WS" ]

    RULE_programa = 0
    RULE_funcion = 1
    RULE_parametros = 2
    RULE_cuerpo = 3
    RULE_asignacion = 4
    RULE_expresion = 5
    RULE_termino = 6
    RULE_factor = 7

    ruleNames =  [ "programa", "funcion", "parametros", "cuerpo", "asignacion", 
                   "expresion", "termino", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    ID=12
    NUMERO=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcion(self):
            return self.getTypedRuleContext(TraductorPyJavaParser.FuncionContext,0)


        def EOF(self):
            return self.getToken(TraductorPyJavaParser.EOF, 0)

        def getRuleIndex(self):
            return TraductorPyJavaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = TraductorPyJavaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.funcion()
            self.state = 17
            self.match(TraductorPyJavaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TraductorPyJavaParser.ID, 0)

        def parametros(self):
            return self.getTypedRuleContext(TraductorPyJavaParser.ParametrosContext,0)


        def cuerpo(self):
            return self.getTypedRuleContext(TraductorPyJavaParser.CuerpoContext,0)


        def getRuleIndex(self):
            return TraductorPyJavaParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)




    def funcion(self):

        localctx = TraductorPyJavaParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(TraductorPyJavaParser.T__0)
            self.state = 20
            self.match(TraductorPyJavaParser.ID)
            self.state = 21
            self.match(TraductorPyJavaParser.T__1)
            self.state = 22
            self.parametros()
            self.state = 23
            self.match(TraductorPyJavaParser.T__2)
            self.state = 24
            self.match(TraductorPyJavaParser.T__3)
            self.state = 25
            self.cuerpo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TraductorPyJavaParser.ID)
            else:
                return self.getToken(TraductorPyJavaParser.ID, i)

        def getRuleIndex(self):
            return TraductorPyJavaParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)




    def parametros(self):

        localctx = TraductorPyJavaParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(TraductorPyJavaParser.ID)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 28
                self.match(TraductorPyJavaParser.T__4)
                self.state = 29
                self.match(TraductorPyJavaParser.ID)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CuerpoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(TraductorPyJavaParser.AsignacionContext,0)


        def expresion(self):
            return self.getTypedRuleContext(TraductorPyJavaParser.ExpresionContext,0)


        def getRuleIndex(self):
            return TraductorPyJavaParser.RULE_cuerpo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCuerpo" ):
                listener.enterCuerpo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCuerpo" ):
                listener.exitCuerpo(self)




    def cuerpo(self):

        localctx = TraductorPyJavaParser.CuerpoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cuerpo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.asignacion()
            self.state = 36
            self.match(TraductorPyJavaParser.T__5)
            self.state = 37
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TraductorPyJavaParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(TraductorPyJavaParser.ExpresionContext,0)


        def getRuleIndex(self):
            return TraductorPyJavaParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = TraductorPyJavaParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(TraductorPyJavaParser.ID)
            self.state = 40
            self.match(TraductorPyJavaParser.T__6)
            self.state = 41
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TraductorPyJavaParser.TerminoContext)
            else:
                return self.getTypedRuleContext(TraductorPyJavaParser.TerminoContext,i)


        def getRuleIndex(self):
            return TraductorPyJavaParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = TraductorPyJavaParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.termino()
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==9:
                self.state = 44
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 45
                self.termino()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TraductorPyJavaParser.FactorContext)
            else:
                return self.getTypedRuleContext(TraductorPyJavaParser.FactorContext,i)


        def getRuleIndex(self):
            return TraductorPyJavaParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)




    def termino(self):

        localctx = TraductorPyJavaParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.factor()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==11:
                self.state = 52
                _la = self._input.LA(1)
                if not(_la==10 or _la==11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 53
                self.factor()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TraductorPyJavaParser.ID, 0)

        def NUMERO(self):
            return self.getToken(TraductorPyJavaParser.NUMERO, 0)

        def expresion(self):
            return self.getTypedRuleContext(TraductorPyJavaParser.ExpresionContext,0)


        def getRuleIndex(self):
            return TraductorPyJavaParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = TraductorPyJavaParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_factor)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(TraductorPyJavaParser.ID)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(TraductorPyJavaParser.NUMERO)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.match(TraductorPyJavaParser.T__1)
                self.state = 62
                self.expresion()
                self.state = 63
                self.match(TraductorPyJavaParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





