import unittest
from cast.analysers.test import MainframeTestAnalysis



class Test(unittest.TestCase):
    
    def test_ok1(self):
        
        analysis = MainframeTestAnalysis()
        analysis.add_dependency(r'C:\ProgramData\CAST\CAST\Extensions\com.castsoftware.mainframe.1.0.0-alpha1')
        analysis.add_selection('binary_depending/pgmok1.cob')
#         analysis.set_verbose()
        analysis.run()
        
        program = analysis.get_object_by_name('PGM1', 'CAST_COBOL_SavedProgram')
        self.assertTrue(program)
        self.assertFalse(analysis.get_violations(program, 'MyCompany_COBOL_Rules.useBinaryForDepending'))

    def test_ko1(self):
        
        analysis = MainframeTestAnalysis()
        analysis.add_dependency(r'C:\ProgramData\CAST\CAST\Extensions\com.castsoftware.mainframe.1.0.0-alpha1')
        analysis.add_selection('binary_depending/pgmko1.cob')
#         analysis.set_verbose()
        analysis.run()
        
        program = analysis.get_object_by_name('PGM1', 'CAST_COBOL_SavedProgram')
        self.assertTrue(program)
        
        # list of violations for the program/rule 
        violations = analysis.get_violations(program, 'MyCompany_COBOL_Rules.useBinaryForDepending')
        self.assertEqual(1, len(violations))
        
        # the first violation
        violation = violations[0]
        
#         print(violation.position)

        # the data declaration containing the occurs depending on a non binary data 
        # starts at line 6
        self.assertEqual(6, violation.position.begin_line)
        

    
if __name__ == '__main__':
    unittest.main()

    