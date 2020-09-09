from cast.analysers import log, mainframe



class UseBinaryInOccursDepending(mainframe.Extension):
    
    def __init__(self):
        self.program = None
        
        # data have sub data so we need a stack
        self.data_stack = []

    def start_program(self, program):
        # memorize the current program to be able to set the violation on it
        log.info('starting program')
        self.program = program

    def end_program(self, _):
        self.program = None
        
    def start_data(self, data):
        self.data_stack.append(data)

    def start_occurs_depending(self, node):
        
        variable = node.get_children()[0]
        
        for depending in variable.get_resolved_datas():
            
            if depending.get_usage() not in ['BINARY', 'COMPUTATIONAL']:
                self.program.save_violation('MyCompany_COBOL_Rules.useBinaryForDepending', self.data_stack[-1].get_position())

    def end_data(self, _):
        self.data_stack.pop()
