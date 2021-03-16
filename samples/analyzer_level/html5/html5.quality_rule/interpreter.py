from cast.analysers import log

class Interpreter:
    
    def __init__(self):
        self.initialize()

    def initialize(self):
        self.while_level = 0
        self.functions_stack = []
        self.jsContent = None

    def start_JsContent(self, ast):
        log.info('start_JsContent ' + str(ast))
        self.jsContent = ast
    
    def start_Function(self, ast):
        log.info('start_Function ' + str(ast))
        self.functions_stack.append(ast)
    
    def start_ArrowFunction(self, ast):
        log.info('start_ArrowFunction ' + str(ast))
        self.functions_stack.append(ast)
    
    def start_Method(self, ast):
        log.info('start_Method ' + str(ast))
        self.functions_stack.append(ast)
    
    def start_FunctionCall(self, ast):
        log.info('start_FunctionCall ' + str(ast))
    
    def start_FunctionCallPart(self, ast):
        log.info('start_FunctionCallPart ' + str(ast))
    
    def start_Identifier(self, ast):
        log.info('start_Identifier ' + str(ast))
        
    def start_AnyStatement(self, ast):    
        log.info('start_AnyStatement ' + str(ast))
        if self.while_level > 0 and ast.is_break_statement():
            if self.functions_stack:
                obj = self.functions_stack[-1].get_kb_object()
            else:
                obj = self.jsContent.get_kb_object()
            if obj:
                obj.save_violation('CAST_Html5Diags_Metric_UseOfBreakInWhile.numberOfBreakInWhile', ast.create_bookmark(self.jsContent.get_file()))

    def start_WhileBlock(self, ast):    
        log.info('start_WhileBlock ' + str(ast))
        self.while_level += 1

    def end_WhileBlock(self, ast):    
        log.info('end_WhileBlock ' + str(ast))
        self.while_level -= 1

    def end_JsContent(self, ast):
        log.info('end_JsContent ' + str(ast))
    
    def end_Function(self, ast):
        log.info('end_Function ' + str(ast))
        self.functions_stack.pop()
    
    def end_ArrowFunction(self, ast):
        log.info('end_ArrowFunction ' + str(ast))
        self.functions_stack.pop()
    
    def end_Method(self, ast):
        log.info('end_Method ' + str(ast))
        self.functions_stack.pop()
    
    def end_FunctionCall(self, ast):
        log.info('end_FunctionCall ' + str(ast))
    
    def end_FunctionCallPart(self, ast):
        log.info('end_FunctionCallPart ' + str(ast))
    
    def end_Identifier(self, ast):
        log.info('end_Identifier ' + str(ast))
        
    def finish(self):
        self.initialize()
        