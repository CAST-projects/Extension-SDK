import unittest
import cast.analysers.test


class TestUnit(unittest.TestCase):
    
    def test_convention(self):
 
        analysis = cast.analysers.test.DotNetTestAnalysis()
        
        analysis.add_selection('Linq2Sql/Linq2Sql.csproj')
        analysis.add_database_table('StudentInfo', 'TSQL')
        analysis.set_verbose()
        
        analysis.run()


if __name__ == "__main__":
    unittest.main()
