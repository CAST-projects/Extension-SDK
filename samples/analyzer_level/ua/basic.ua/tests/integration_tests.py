import unittest
import tempfile
import cast.analysers.test


class TestIntegration(unittest.TestCase):
 
    def test_analyse_one_file(self):
  
        # we create a temporary file with some content
        f = tempfile.NamedTemporaryFile(mode='w+', suffix='.ext1', delete=False)
        f.write("""
// this file is really interesting... or not

        """)
        f.close()

        # we start a simulated analysis selecting an universal analyser named 'MyLanguage'
        analysis = cast.analysers.test.UATestAnalysis('MyLanguage')
  
        # having this file as input
        analysis.add_selection(f.name)
        analysis.set_verbose(True)
        
        # we run... 
        analysis.run()

        # here we check that we have constructed one object :
        self.assertTrue(analysis.get_objects_by_name('name1', 'MyLanguage_Object1'))


if __name__ == "__main__":
    unittest.main()
