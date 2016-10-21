import unittest
import cast.analysers.test


class Test(unittest.TestCase):
    def testRegisterPlugin(self):
        # create a DotNet analysis
        analysis = cast.analysers.test.DotNetTestAnalysis()
        # DotNet need a selection of a csproj or sln
        analysis.add_selection('AProject/AProject.csproj')
        analysis.set_verbose()
        analysis.run()
        
if __name__ == "__main__":
    unittest.main()
