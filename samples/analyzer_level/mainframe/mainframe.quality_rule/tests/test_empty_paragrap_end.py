import unittest
from cast.analysers.test import MainframeTestAnalysis



class Test(unittest.TestCase):
    
    def test_ok1(self):
        
        analysis = MainframeTestAnalysis()
        analysis.add_dependency(r'C:\ProgramData\CAST\CAST\Extensions\com.castsoftware.mainframe.1.0.0-alpha1')
        analysis.add_selection('empty_paragraph_end/pgmok1.cob')
#         analysis.set_verbose()
        analysis.run()
        
        program = analysis.get_object_by_name('PGM1', 'CAST_COBOL_SavedProgram')
        self.assertTrue(program)
        self.assertFalse(analysis.get_violations(program, 'MyCompany_COBOL_Rules.sectionEndParagraph'))

    def test_ok2(self):
        
        analysis = MainframeTestAnalysis()
        analysis.add_dependency(r'C:\ProgramData\CAST\CAST\Extensions\com.castsoftware.mainframe.1.0.0-alpha1')
        analysis.add_selection('empty_paragraph_end/pgmok2.cob')
#         analysis.set_verbose()
        analysis.run()
        
        program = analysis.get_object_by_name('PGM1', 'CAST_COBOL_SavedProgram')
        self.assertTrue(program)
        self.assertFalse(analysis.get_violations(program, 'MyCompany_COBOL_Rules.sectionEndParagraph'))

    def test_ok3(self):
        
        analysis = MainframeTestAnalysis()
        analysis.add_dependency(r'C:\ProgramData\CAST\CAST\Extensions\com.castsoftware.mainframe.1.0.0-alpha1')
        analysis.add_selection('empty_paragraph_end/pgmok3.cob')
#         analysis.set_verbose()
        analysis.run()
        
        program = analysis.get_object_by_name('PGM1', 'CAST_COBOL_SavedProgram')
        self.assertTrue(program)
        self.assertFalse(analysis.get_violations(program, 'MyCompany_COBOL_Rules.sectionEndParagraph'))

    def test_ok4(self):
        
        analysis = MainframeTestAnalysis()
        analysis.add_dependency(r'C:\ProgramData\CAST\CAST\Extensions\com.castsoftware.mainframe.1.0.0-alpha1')
        analysis.add_selection('empty_paragraph_end/pgmok4.cob')
#         analysis.set_verbose()
        analysis.run()
        
        program = analysis.get_object_by_name('PGM1', 'CAST_COBOL_SavedProgram')
        self.assertTrue(program)
        self.assertFalse(analysis.get_violations(program, 'MyCompany_COBOL_Rules.sectionEndParagraph'))

    def test_ko1(self):
        
        analysis = MainframeTestAnalysis()
        analysis.add_dependency(r'C:\ProgramData\CAST\CAST\Extensions\com.castsoftware.mainframe.1.0.0-alpha1')
        analysis.add_selection('empty_paragraph_end/pgmko1.cob')
#         analysis.set_verbose()
        analysis.run()
        
        program = analysis.get_object_by_name('PGM1', 'CAST_COBOL_SavedProgram')
        self.assertTrue(program)
        self.assertTrue(analysis.get_violations(program, 'MyCompany_COBOL_Rules.sectionEndParagraph'))


    def test_ko2(self):
        
        analysis = MainframeTestAnalysis()
        analysis.add_dependency(r'C:\ProgramData\CAST\CAST\Extensions\com.castsoftware.mainframe.1.0.0-alpha1')
        analysis.add_selection('empty_paragraph_end/pgmko2.cob')
#         analysis.set_verbose()
        analysis.run()
        
        program = analysis.get_object_by_name('PGM1', 'CAST_COBOL_SavedProgram')
        self.assertTrue(program)
        self.assertTrue(analysis.get_violations(program, 'MyCompany_COBOL_Rules.sectionEndParagraph'))

    def test_ko3(self):
        
        analysis = MainframeTestAnalysis()
        analysis.add_dependency(r'C:\ProgramData\CAST\CAST\Extensions\com.castsoftware.mainframe.1.0.0-alpha1')
        analysis.add_selection('empty_paragraph_end/pgmko3.cob')
#         analysis.set_verbose()
        analysis.run()
        
        program = analysis.get_object_by_name('PGM1', 'CAST_COBOL_SavedProgram')
        self.assertTrue(program)
        self.assertTrue(analysis.get_violations(program, 'MyCompany_COBOL_Rules.sectionEndParagraph'))

    
if __name__ == '__main__':
    
    unittest.main()