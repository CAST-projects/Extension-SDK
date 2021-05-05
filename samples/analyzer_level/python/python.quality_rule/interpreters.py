from cast.analysers import log


class SimpleInfoPrint:
    """
    Interpreter showing how to collect statistical data
    for the entire project.

    The interpreter has to include the following
    elements at least:

        - An '__init__' method accepting a 'module' parameter. This 'module'
        essentially represents a Python file.

    Optionally it can be added

        - An 'on_end' method has two usages:
            - cross-check collected data at module level
            - delete collected data at module level if not further necessary
    """

    def __init__(self, module):
        self.module = module
        self.nb_calls = 0

    def start_MethodCall(self, ast):
        log.info("[start_MethodCall] {}".format(ast.get_type()))

        # print the AST of a MethodCall node
        print_tree(ast)

        # get the arguments
        arg0 = ast.get_argument(0, None)
        log.info("Arguments: {}".format(arg0))

    def end_MethodCall(self, ast):
        log.info("[end_MethodCall] {}".format(ast.get_type()))
    
    def start_Return(self, ast):
        log.debug("[start_Return] {}".format(ast.get_type()))

    def on_end(self):
        log.info("[on_end] do nothing ...")

    
class RuleAllContainingOnlyStrings:
    """
    A typical linting rule from pylint:

    References:
        https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/E0604.html
        https://stackoverflow.com/questions/41860105/why-should-all-only-contain-string-objects
    """

    def __init__(self, module):
        self.__module = module

    def start_Assignment(self, assig):
        
        # we can inspect the ast to decide
        # which nodes are convenient for analysis
        print_tree(assig)

        right = assig.get_right_expression()
        left = assig.get_left_expression()
        if not left.get_type() == 'Identifier':
            return
        
        varname = left.get_name()
        expression_type = str(right.get_type())
        seen_violation = False
        if varname == '__all__' and expression_type == 'Array':
            values = right.get_values()
            for v in values:
                # case 1: argument is a string literal
                if v.get_type() == 'Constant' and v.is_constant_string():
                    continue
                
                # case 2: when argument is a variable and resolves to a symbol
                if v.get_type() == 'Identifier':
                    resolutions = v.get_resolutions()
                    for r in resolutions:
                        if r.is_class() or r.is_function():
                            seen_violation = True
                            break

                if seen_violation:
                    break

        if not seen_violation:
            return

        # add violation to current module
        module = self.get_module()
        module.add_violation('CAST_Python_Rule.PREFIX_PrototypedQualityRule', assig)
        log.info("Added violation to module {}".format(module.get_fullname()))

    def on_end(self):
        """optional callback function when analysis module is finished"""
        pass

    def get_module(self):
        return self.__module


def print_tree(ast):
    """Utility for printing the ast in debug mode"""
    import sys
    from io import StringIO

    orig_stdout = sys.stdout
    s = StringIO()
    sys.stdout = s
    ast.print_tree()
    log.debug("printing ast ...\n{}".format(s.getvalue()))
    sys.stdout = orig_stdout

