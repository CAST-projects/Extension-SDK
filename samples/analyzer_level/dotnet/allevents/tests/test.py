'''
Created on 14 mars 2015

@author: MRO
'''
import unittest
import cast.analysers.test


class Test(unittest.TestCase):

    def test(self):
        
        analysis = cast.analysers.test.DotNetTestAnalysis()
        analysis.add_selection('CodeFirstAnnotationInheritance/SchoolDomainClasses.csproj')
        analysis.set_verbose()
        analysis.run()
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()