import unittest
import cast.analysers.test


def launch(path):
    analysis = cast.analysers.test.UATestAnalysis('Python')
    analysis.add_selection(path)

    # add dependency to python extension
    analysis.add_dependency(r'C:\ProgramData\CAST\CAST\Extensions\com.castsoftware.python.1.4.0-beta11000303')
    # analysis.add_dependency(r'E:\plugins2\Python\com.castsoftware.python')

    analysis.set_verbose(True)
    analysis.run()
    return analysis


class TestIntegration(unittest.TestCase):

    def test_integration_01(self):
        """
        Test showing how to verify the number of python functions/methods
        created by the analyzer. Some functions are created internally
        (builtin functions, etc). These can be filtered out as shown below.
        """

        analysis = launch(r'samples/test01')

        # get all Python functions (a dict)
        functions = analysis.get_objects_by_category('CAST_Python_Method')
        print("The total number of functions/methods: {}".format(len(functions)))

        # remove external functions/methods
        functions = [f for f in functions.values() if f.get_value('POSITIONABLE.POSITIONS')]
        self.assertEqual(3, len(functions))  # expected number

    def test_integration_02(self):
        """
        Test showing how to verify the presence of a custom quality rule
        violation in a Python object (in this case a Python Module object)
        """
        
        analysis = launch(r'samples/test02')

        # foo.py
        module = analysis.get_object_by_name('foo.py', 'CAST_Python_SourceCode')
        has_violation = module.get_value('CAST_Python_Rule.PREFIX_PrototypedQualityRule')
        self.assertFalse(has_violation)

        # with_violation.py
        module = analysis.get_object_by_name('with_violation.py', 'CAST_Python_SourceCode')
        # the presence of a violation is marked in a property with a non-zero number
        has_violation = module.get_value('CAST_Python_Rule.PREFIX_PrototypedQualityRule')
        self.assertTrue(has_violation)


if __name__ == "__main__":
    unittest.main()
