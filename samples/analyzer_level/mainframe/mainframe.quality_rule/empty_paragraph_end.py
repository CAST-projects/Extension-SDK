from cast.analysers import log, mainframe


class EmptyParagraphEndOfSection(mainframe.Extension):
    
    def __init__(self):
        self.program = None

    def start_program(self, program):
        self.program = program

    def end_program(self, _):
        self.program = None
        
    def start_section(self, section):
        last_paragraph = section.get_children()[-1]
        
        if 'paragraph' == last_paragraph.get_kind():
            
            children = last_paragraph.get_children()
            if len(children) > 1:
                # violation test_ko2
                self.program.save_violation('MyCompany_COBOL_Rules.sectionEndParagraph', section.get_position())
            
            elif len(children) == 1:
                
                kind = children[0].get_kind()
                if kind not in ['exit', 'stop_run', 'goback']:
                    self.program.save_violation('MyCompany_COBOL_Rules.sectionEndParagraph', section.get_position())
        else:
            # violation test_ko1
            self.program.save_violation('MyCompany_COBOL_Rules.sectionEndParagraph', section.get_position())
            
            
            
        