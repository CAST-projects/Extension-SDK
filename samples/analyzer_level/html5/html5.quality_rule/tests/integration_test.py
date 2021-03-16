import unittest
import cast.analysers.test


class TestIntegration(unittest.TestCase):

    def test_integration_01(self):

        analysis = cast.analysers.test.UATestAnalysis('HTML5')
        analysis.add_selection('test1')
        # add dependecy to html5
        analysis.add_dependency(r'C:\ProgramData\CAST\CAST\Extensions\com.castsoftware.html5.2.1.1-funcrel')
        analysis.set_verbose(True)
        analysis.run()
        
        f = analysis.get_object_by_name('f', 'CAST_HTML5_JavaScript_Function')
        self.assertTrue(f)
        _value = f.get_value('CAST_Html5Diags_Metric_UseOfBreakInWhile.numberOfBreakInWhile')
        self.assertEqual('1', _value)


if __name__ == "__main__":
    unittest.main()
