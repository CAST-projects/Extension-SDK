import unittest
import cast.analysers.test


class TestIntegration(unittest.TestCase):

    def test1(self):

        analysis = cast.analysers.test.JEETestAnalysis()

        analysis.add_selection('coffeebean')

        analysis.set_verbose()
        analysis.run()

if __name__ == "__main__":
    unittest.main()
