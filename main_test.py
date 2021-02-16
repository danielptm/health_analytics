import unittest
from Analyze import Analyze


class AnalyzeTest(unittest.TestCase):

    def testhi(self):
        result = Analyze().print()
        self.assertEqual("hi", result)

if __name__ == '__main__':
    unittest.main()