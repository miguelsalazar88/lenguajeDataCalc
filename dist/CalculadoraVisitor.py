# Generated from Calculadora.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete generic visitor for a parse tree produced by CalculadoraParser.

class CalculadoraVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculadoraParser#parse.
    def visitParse(self, ctx:CalculadoraParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#from_input.
    def visitFrom_input(self, ctx:CalculadoraParser.From_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#from_file.
    def visitFrom_file(self, ctx:CalculadoraParser.From_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#stat.
    def visitStat(self, ctx:CalculadoraParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#compound_stat.
    def visitCompound_stat(self, ctx:CalculadoraParser.Compound_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#simple_stat.
    def visitSimple_stat(self, ctx:CalculadoraParser.Simple_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#matrices.
    def visitMatrices(self, ctx:CalculadoraParser.MatricesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#inverse.
    def visitInverse(self, ctx:CalculadoraParser.InverseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#matmul.
    def visitMatmul(self, ctx:CalculadoraParser.MatmulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#matsum.
    def visitMatsum(self, ctx:CalculadoraParser.MatsumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#matrest.
    def visitMatrest(self, ctx:CalculadoraParser.MatrestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#transpose.
    def visitTranspose(self, ctx:CalculadoraParser.TransposeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#for_stat.
    def visitFor_stat(self, ctx:CalculadoraParser.For_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#while_stat.
    def visitWhile_stat(self, ctx:CalculadoraParser.While_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#range.
    def visitRange(self, ctx:CalculadoraParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#stat_block.
    def visitStat_block(self, ctx:CalculadoraParser.Stat_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#assignment.
    def visitAssignment(self, ctx:CalculadoraParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#importar.
    def visitImportar(self, ctx:CalculadoraParser.ImportarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#retornar.
    def visitRetornar(self, ctx:CalculadoraParser.RetornarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#plotExpr.
    def visitPlotExpr(self, ctx:CalculadoraParser.PlotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#sqrtExpr.
    def visitSqrtExpr(self, ctx:CalculadoraParser.SqrtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#atomExpr.
    def visitAtomExpr(self, ctx:CalculadoraParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#orExpr.
    def visitOrExpr(self, ctx:CalculadoraParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:CalculadoraParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#relationalExpr.
    def visitRelationalExpr(self, ctx:CalculadoraParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#parExpr.
    def visitParExpr(self, ctx:CalculadoraParser.ParExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#notExpr.
    def visitNotExpr(self, ctx:CalculadoraParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:CalculadoraParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#multiplicationExpr.
    def visitMultiplicationExpr(self, ctx:CalculadoraParser.MultiplicationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#powExpr.
    def visitPowExpr(self, ctx:CalculadoraParser.PowExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#equalityExpr.
    def visitEqualityExpr(self, ctx:CalculadoraParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#trigoExpr.
    def visitTrigoExpr(self, ctx:CalculadoraParser.TrigoExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#andExpr.
    def visitAndExpr(self, ctx:CalculadoraParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#numberAtom.
    def visitNumberAtom(self, ctx:CalculadoraParser.NumberAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#booleanAtom.
    def visitBooleanAtom(self, ctx:CalculadoraParser.BooleanAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#stringAtom.
    def visitStringAtom(self, ctx:CalculadoraParser.StringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#arrayAtom.
    def visitArrayAtom(self, ctx:CalculadoraParser.ArrayAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#accessToarray.
    def visitAccessToarray(self, ctx:CalculadoraParser.AccessToarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#accessVariable.
    def visitAccessVariable(self, ctx:CalculadoraParser.AccessVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#spaceAtom.
    def visitSpaceAtom(self, ctx:CalculadoraParser.SpaceAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#noneAtom.
    def visitNoneAtom(self, ctx:CalculadoraParser.NoneAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#array.
    def visitArray(self, ctx:CalculadoraParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#accessarray.
    def visitAccessarray(self, ctx:CalculadoraParser.AccessarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#variable.
    def visitVariable(self, ctx:CalculadoraParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#parametro.
    def visitParametro(self, ctx:CalculadoraParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#trigo.
    def visitTrigo(self, ctx:CalculadoraParser.TrigoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#raiz.
    def visitRaiz(self, ctx:CalculadoraParser.RaizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#imprimir.
    def visitImprimir(self, ctx:CalculadoraParser.ImprimirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#plot.
    def visitPlot(self, ctx:CalculadoraParser.PlotContext):
        return self.visitChildren(ctx)



del CalculadoraParser