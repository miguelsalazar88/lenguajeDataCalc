# Generated from Calculadora.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete listener for a parse tree produced by CalculadoraParser.
class CalculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by CalculadoraParser#parse.
    def enterParse(self, ctx:CalculadoraParser.ParseContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#parse.
    def exitParse(self, ctx:CalculadoraParser.ParseContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#from_input.
    def enterFrom_input(self, ctx:CalculadoraParser.From_inputContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#from_input.
    def exitFrom_input(self, ctx:CalculadoraParser.From_inputContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#from_file.
    def enterFrom_file(self, ctx:CalculadoraParser.From_fileContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#from_file.
    def exitFrom_file(self, ctx:CalculadoraParser.From_fileContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#stat.
    def enterStat(self, ctx:CalculadoraParser.StatContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#stat.
    def exitStat(self, ctx:CalculadoraParser.StatContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#compound_stat.
    def enterCompound_stat(self, ctx:CalculadoraParser.Compound_statContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#compound_stat.
    def exitCompound_stat(self, ctx:CalculadoraParser.Compound_statContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#simple_stat.
    def enterSimple_stat(self, ctx:CalculadoraParser.Simple_statContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#simple_stat.
    def exitSimple_stat(self, ctx:CalculadoraParser.Simple_statContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#matrices.
    def enterMatrices(self, ctx:CalculadoraParser.MatricesContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#matrices.
    def exitMatrices(self, ctx:CalculadoraParser.MatricesContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#inverse.
    def enterInverse(self, ctx:CalculadoraParser.InverseContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#inverse.
    def exitInverse(self, ctx:CalculadoraParser.InverseContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#matmul.
    def enterMatmul(self, ctx:CalculadoraParser.MatmulContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#matmul.
    def exitMatmul(self, ctx:CalculadoraParser.MatmulContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#matsum.
    def enterMatsum(self, ctx:CalculadoraParser.MatsumContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#matsum.
    def exitMatsum(self, ctx:CalculadoraParser.MatsumContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#matrest.
    def enterMatrest(self, ctx:CalculadoraParser.MatrestContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#matrest.
    def exitMatrest(self, ctx:CalculadoraParser.MatrestContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#transpose.
    def enterTranspose(self, ctx:CalculadoraParser.TransposeContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#transpose.
    def exitTranspose(self, ctx:CalculadoraParser.TransposeContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#for_stat.
    def enterFor_stat(self, ctx:CalculadoraParser.For_statContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#for_stat.
    def exitFor_stat(self, ctx:CalculadoraParser.For_statContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#while_stat.
    def enterWhile_stat(self, ctx:CalculadoraParser.While_statContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#while_stat.
    def exitWhile_stat(self, ctx:CalculadoraParser.While_statContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#range.
    def enterRange(self, ctx:CalculadoraParser.RangeContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#range.
    def exitRange(self, ctx:CalculadoraParser.RangeContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#stat_block.
    def enterStat_block(self, ctx:CalculadoraParser.Stat_blockContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#stat_block.
    def exitStat_block(self, ctx:CalculadoraParser.Stat_blockContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#assignment.
    def enterAssignment(self, ctx:CalculadoraParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#assignment.
    def exitAssignment(self, ctx:CalculadoraParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#importar.
    def enterImportar(self, ctx:CalculadoraParser.ImportarContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#importar.
    def exitImportar(self, ctx:CalculadoraParser.ImportarContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#retornar.
    def enterRetornar(self, ctx:CalculadoraParser.RetornarContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#retornar.
    def exitRetornar(self, ctx:CalculadoraParser.RetornarContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#plotExpr.
    def enterPlotExpr(self, ctx:CalculadoraParser.PlotExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#plotExpr.
    def exitPlotExpr(self, ctx:CalculadoraParser.PlotExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#sqrtExpr.
    def enterSqrtExpr(self, ctx:CalculadoraParser.SqrtExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#sqrtExpr.
    def exitSqrtExpr(self, ctx:CalculadoraParser.SqrtExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#atomExpr.
    def enterAtomExpr(self, ctx:CalculadoraParser.AtomExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#atomExpr.
    def exitAtomExpr(self, ctx:CalculadoraParser.AtomExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#orExpr.
    def enterOrExpr(self, ctx:CalculadoraParser.OrExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#orExpr.
    def exitOrExpr(self, ctx:CalculadoraParser.OrExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:CalculadoraParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:CalculadoraParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#relationalExpr.
    def enterRelationalExpr(self, ctx:CalculadoraParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#relationalExpr.
    def exitRelationalExpr(self, ctx:CalculadoraParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#parExpr.
    def enterParExpr(self, ctx:CalculadoraParser.ParExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#parExpr.
    def exitParExpr(self, ctx:CalculadoraParser.ParExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#notExpr.
    def enterNotExpr(self, ctx:CalculadoraParser.NotExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#notExpr.
    def exitNotExpr(self, ctx:CalculadoraParser.NotExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#unaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:CalculadoraParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#unaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:CalculadoraParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#multiplicationExpr.
    def enterMultiplicationExpr(self, ctx:CalculadoraParser.MultiplicationExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#multiplicationExpr.
    def exitMultiplicationExpr(self, ctx:CalculadoraParser.MultiplicationExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#powExpr.
    def enterPowExpr(self, ctx:CalculadoraParser.PowExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#powExpr.
    def exitPowExpr(self, ctx:CalculadoraParser.PowExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#equalityExpr.
    def enterEqualityExpr(self, ctx:CalculadoraParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#equalityExpr.
    def exitEqualityExpr(self, ctx:CalculadoraParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#trigoExpr.
    def enterTrigoExpr(self, ctx:CalculadoraParser.TrigoExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#trigoExpr.
    def exitTrigoExpr(self, ctx:CalculadoraParser.TrigoExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#andExpr.
    def enterAndExpr(self, ctx:CalculadoraParser.AndExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#andExpr.
    def exitAndExpr(self, ctx:CalculadoraParser.AndExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#numberAtom.
    def enterNumberAtom(self, ctx:CalculadoraParser.NumberAtomContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#numberAtom.
    def exitNumberAtom(self, ctx:CalculadoraParser.NumberAtomContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#booleanAtom.
    def enterBooleanAtom(self, ctx:CalculadoraParser.BooleanAtomContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#booleanAtom.
    def exitBooleanAtom(self, ctx:CalculadoraParser.BooleanAtomContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#stringAtom.
    def enterStringAtom(self, ctx:CalculadoraParser.StringAtomContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#stringAtom.
    def exitStringAtom(self, ctx:CalculadoraParser.StringAtomContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#arrayAtom.
    def enterArrayAtom(self, ctx:CalculadoraParser.ArrayAtomContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#arrayAtom.
    def exitArrayAtom(self, ctx:CalculadoraParser.ArrayAtomContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#accessToarray.
    def enterAccessToarray(self, ctx:CalculadoraParser.AccessToarrayContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#accessToarray.
    def exitAccessToarray(self, ctx:CalculadoraParser.AccessToarrayContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#accessVariable.
    def enterAccessVariable(self, ctx:CalculadoraParser.AccessVariableContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#accessVariable.
    def exitAccessVariable(self, ctx:CalculadoraParser.AccessVariableContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#spaceAtom.
    def enterSpaceAtom(self, ctx:CalculadoraParser.SpaceAtomContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#spaceAtom.
    def exitSpaceAtom(self, ctx:CalculadoraParser.SpaceAtomContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#noneAtom.
    def enterNoneAtom(self, ctx:CalculadoraParser.NoneAtomContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#noneAtom.
    def exitNoneAtom(self, ctx:CalculadoraParser.NoneAtomContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#array.
    def enterArray(self, ctx:CalculadoraParser.ArrayContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#array.
    def exitArray(self, ctx:CalculadoraParser.ArrayContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#accessarray.
    def enterAccessarray(self, ctx:CalculadoraParser.AccessarrayContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#accessarray.
    def exitAccessarray(self, ctx:CalculadoraParser.AccessarrayContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#variable.
    def enterVariable(self, ctx:CalculadoraParser.VariableContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#variable.
    def exitVariable(self, ctx:CalculadoraParser.VariableContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#parametro.
    def enterParametro(self, ctx:CalculadoraParser.ParametroContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#parametro.
    def exitParametro(self, ctx:CalculadoraParser.ParametroContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#trigo.
    def enterTrigo(self, ctx:CalculadoraParser.TrigoContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#trigo.
    def exitTrigo(self, ctx:CalculadoraParser.TrigoContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#raiz.
    def enterRaiz(self, ctx:CalculadoraParser.RaizContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#raiz.
    def exitRaiz(self, ctx:CalculadoraParser.RaizContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#imprimir.
    def enterImprimir(self, ctx:CalculadoraParser.ImprimirContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#imprimir.
    def exitImprimir(self, ctx:CalculadoraParser.ImprimirContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#plot.
    def enterPlot(self, ctx:CalculadoraParser.PlotContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#plot.
    def exitPlot(self, ctx:CalculadoraParser.PlotContext):
        pass



del CalculadoraParser