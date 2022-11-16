import sys
import math
import matplotlib.pyplot as plt
import numpy as np
from antlr4 import *
from dist.CalculadoraLexer import CalculadoraLexer
from dist.CalculadoraParser import CalculadoraParser
from dist.CalculadoraVisitor import CalculadoraVisitor

class CalcVisitor(CalculadoraVisitor):

    memoria = dict()

    def __init__(self):
        self.memoria = dict()

    # Imprimir algo
    def visitImprimir(self, ctx:CalculadoraParser.ImprimirContext):
        val = str(self.visit(ctx.expr()))
        print(val.replace('"',''))

    def visitWhile_stat(self, ctx:CalculadoraParser.While_statContext):
        condition = self.visit(ctx.expr())
        print(condition)
        while(condition):
            self.visit(ctx.stat_block())
            condition = self.visit(ctx.expr())

    # Visit a parse tree produced by CalculadoraParser#for_stat.
    def visitFor_stat(self, ctx:CalculadoraParser.For_statContext):
        var = ctx.ID().getText()
        if ctx.range_() is not None:
            r = self.visit(ctx.range_())
        elif ctx.variable() is not None:
            var = self.visit(ctx.variable())
            r = range(len(var))
            print(r)
        else:
            r = range(len(self.visit(ctx.array())))
            print(r)
        
        for i in r:
            self.memoria[var] = i
            self.visit(ctx.stat_block())

    def visitRange(self, ctx:CalculadoraParser.RangeContext):
        if ctx.COMMA() is not None:
            abajo = int(ctx.INT(0).getText())
            arriba = int(ctx.INT(1).getText())
            return range(abajo,arriba)
        else:
            num = int(ctx.INT(0).getText())
            return range(num)
        
    # Visit a parse tree produced by CalculadoraParser#matmul.
    def visitMatmul(self, ctx:CalculadoraParser.MatmulContext):
        arr1 = self.visit(ctx.atom(0))
        arr2 = self.visit(ctx.atom(1))
        arr3 = np.matmul(arr1,arr2)
        print(arr3)
        return arr3


    # Visit a parse tree produced by CalculadoraParser#matsum.
    def visitMatsum(self, ctx:CalculadoraParser.MatsumContext):
        arr1 = self.visit(ctx.atom(0))
        arr2 = self.visit(ctx.atom(1))
        arr3 = np.add(arr1,arr2)
        print(arr3)
        return arr3


    # Visit a parse tree produced by CalculadoraParser#matrest.
    def visitMatrest(self, ctx:CalculadoraParser.MatrestContext):
        arr1 = self.visit(ctx.atom(0))
        arr2 = self.visit(ctx.atom(1))
        arr3 = np.subtract(arr1,arr2)
        print(arr3)
        return arr3


    # Visit a parse tree produced by CalculadoraParser#transpose.
    def visitTranspose(self, ctx:CalculadoraParser.TransposeContext):
        arr = self.visit(ctx.atom())
        arrT = np.transpose(arr)
        print(arrT)
        return arrT

    # Visit a parse tree produced by CalculadoraParser#inverse.
    def visitInverse(self, ctx:CalculadoraParser.InverseContext):
        arr = self.visit(ctx.atom())
        arrI = np.linalg.inv(arr)
        print(arrI)
        return arrI


    def visitSimple_stat(self, ctx:CalculadoraParser.Simple_statContext):
        return self.visitChildren(ctx)

    def visitParExpr(self, ctx:CalculadoraParser.ParExprContext):
            return self.visit(ctx.expr())
    
    # Expresión Booleana Not
    def visitNotExpr(self, ctx:CalculadoraParser.NotExprContext):
        value = self.visit(ctx.expr())
        return not value

    # Menos unario -(expr)  
    def visitUnaryMinusExpr(self, ctx:CalculadoraParser.UnaryMinusExprContext):
        value = self.visit(ctx.expr())
        value = value * -1
        return value

    # Visit a parse tree produced by CalculadoraParser#powExpr.
    def visitPowExpr(self, ctx:CalculadoraParser.PowExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return math.pow(left,right)
    
    # Multiplicación, División y Módulo
    def visitMultiplicationExpr(self, ctx:CalculadoraParser.MultiplicationExprContext):
        if ctx.op.type == CalculadoraParser.MULT:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            return left*right
        elif ctx.op.type == CalculadoraParser.DIV:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            return left/right
        else:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            return left%right
    
    # Revisar este
    # Visit a parse tree produced by CalculadoraParser#atomExpr.
    def visitAtomExpr(self, ctx:CalculadoraParser.AtomExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CalculadoraParser#numberAtom.
    def visitNumberAtom(self, ctx:CalculadoraParser.NumberAtomContext):
        if ctx.INT() is not None:
            return int(ctx.getText())
        elif ctx.FLOAT() is not None:
            return float(ctx.getText())


    # Visit a parse tree produced by CalculadoraParser#booleanAtom.
    def visitBooleanAtom(self, ctx:CalculadoraParser.BooleanAtomContext):
        if ctx.TRUE() is not None:
            return True
        elif ctx.FALSE() is not None:
            return False


    # Visit a parse tree produced by CalculadoraParser#stringAtom.
    def visitStringAtom(self, ctx:CalculadoraParser.StringAtomContext):
        return str(ctx.getText())


    # Visit a parse tree produced by CalculadoraParser#arrayAtom.
    def visitArrayAtom(self, ctx:CalculadoraParser.ArrayAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#accessToarray.
    def visitAccessToarray(self, ctx:CalculadoraParser.AccessToarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#accessVariable.
    def visitAccessVariable(self, ctx:CalculadoraParser.AccessVariableContext):
        return self.visitChildren(ctx)



    def visitAdditiveExpr(self, ctx:CalculadoraParser.AdditiveExprContext):
        if ctx.op.type == CalculadoraParser.PLUS:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            return left+right
        if ctx.op.type == CalculadoraParser.MINUS:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            return left-right

    # None o valor nulo
    def visitNoneAtom(self, ctx:CalculadoraParser.NoneAtomContext):
        return None

    # Creacion de arreglos
    def visitArray(self, ctx:CalculadoraParser.ArrayContext):
        arreglo = []
        items = ctx.expr()
        for item in items:
            value = self.visit(item)
            arreglo.append(value)
        return np.array(arreglo)


    # Visit a parse tree produced by CalculadoraParser#accessarray.
    def visitAccessarray(self, ctx:CalculadoraParser.AccessarrayContext):
        varText = ctx.variable().getText()
        index = self.visit(ctx.expr())
        if varText in self.memoria and isinstance(self.memoria[varText],list) and type(index) is int:
            variable = self.memoria[varText]
            return variable[index]
        else:
            print("Variable no existe o no es iterable.")


    # Visit a parse tree produced by CalculadoraParser#variable.
    def visitVariable(self, ctx:CalculadoraParser.VariableContext):
        key = str(ctx.getText())
        if key in self.memoria:
            return self.memoria[key]
        else:
            print('Error: Variable no encontrada')
    # Visit a parse tree produced by CalculadoraParser#parametro.
    def visitParametro(self, ctx:CalculadoraParser.ParametroContext):
        return self.visitChildren(ctx)


    def visitTrigo(self, ctx:CalculadoraParser.TrigoContext):
        expresion = self.visit(ctx.expr())
        if ctx.SIN() is not None:
            return math.sin(expresion)
        elif ctx.COS() is not None:
            return math.cos(expresion)
        elif ctx.TAN() is not None:
            return math.tan(expresion)
        elif ctx.ASIN() is not None:
            return math.asin(expresion)
        elif ctx.ACOS() is not None:
            return math.acos(expresion)
        else:
            return math.atan(expresion)

    # Visit a parse tree produced by CalculadoraParser#raiz.
    def visitRaiz(self, ctx:CalculadoraParser.RaizContext):
        val = self.visit(ctx.expr())
        return math.sqrt(val)
        
    def visitNotExpr(self, ctx:CalculadoraParser.NotExprContext):
        print('Aca estamos')
        expression = self.visit(ctx.expr(0))
        print(f'Normal: {expression}')
        expression =  not expression
        print(f'Negada: {expression}')
        return expression

    # Visit a parse tree produced by CalculadoraParser#assignment.
    def visitAssignment(self, ctx:CalculadoraParser.AssignmentContext):
        name  = str(ctx.variable().getText())
        value = self.visit(ctx.expr())
        self.memoria[name] = value

    def visitPlot(self, ctx:CalculadoraParser.PlotContext):
        if len(ctx.atom()) == 1:
            x = self.visit(ctx.atom(0))
            plt.plot(x)
            plt.show()
        if len(ctx.atom()) == 2:
            x = self.visit(ctx.atom(0))
            y = self.visit(ctx.atom(1))
            plt.scatter(x,y)
            plt.show()


    
    # Comparación entre LTEQ|GTEQ|LT|GT
    def visitRelationalExpr(self, ctx:CalculadoraParser.RelationalExprContext):
        
        if ctx.op.type == CalculadoraParser.LTEQ:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            return left <= right
        elif ctx.op.type == CalculadoraParser.GTEQ:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            return left >= right
        
        elif ctx.op.type == CalculadoraParser.LT:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            return left < right

        else:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            return left > right
    
    
    


if __name__ == '__main__':

    print('-----DataCalc-----')
    
    if len(sys.argv) > 1:
        try:
            input_stream = FileStream(sys.argv[1])
        except Exception as e:
            raise Exception('Archivo no encontrado')
        
        visitor = CalcVisitor()
        lexer=CalculadoraLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CalculadoraParser(stream)
        tree = parser.from_file()
        result = visitor.visit(tree)

    else:
    
        visitor = CalcVisitor()
        while(True):
            print('>>>', end='', flush=True)
            e = sys.stdin.readline().strip()
            if 'exit()' == e:
                break
            input_stream = InputStream(e)
            lexer = CalculadoraLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = CalculadoraParser(stream)
            tree = parser.stat()
            result = visitor.visit(tree)
            if result is not None:
                print(result)