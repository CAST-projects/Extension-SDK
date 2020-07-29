from cast.analysers import log, mainframe


class State:
    
    def __init__(self):
        # paragraphs by name
        self.paragraphs = {}


class DoNotRedefineParagraph(mainframe.Extension):
    
    def __init__(self):
        self.program = None
        # section paragraph are embedded so we use a stack of State
        self.stack = []

    def start_program(self, program):
        self.stack.clear()
        self.program = program

    def end_program(self, _):
        self.stack.clear()
        self.program = None
        
    def start_division(self, division):
        if division.get_name() == 'Procedure Division':
            self.stack.append(State())
    
    def start_section(self, _):
        
        # section so start a new state
        self.stack.append(State())

    def end_section(self, _):
        # pop state
        self.stack.pop()
    
    def start_paragraph(self, paragraph):
        
        name = paragraph.get_name()
        state = self.stack[-1]
        
        if name in state.paragraphs:
            # violation
            log.debug('Violation at position %s' % str(paragraph.get_position()))
            self.program.save_violation('MyCompany_COBOL_Rules.paragraphRedefinition', paragraph.get_position())
        
        state.paragraphs[name] = paragraph
        
    
        
