import unittest
from Analyze import Analyze


class AnalyzeTest(unittest.TestCase):

    def test_getlines(self):
        analyze = Analyze()
        result = analyze.readfile()
        lines = analyze.get_lines(result)
        self.assertEqual(360, len(lines))

    def test_getobjects(self):
        analyze = Analyze()
        result = analyze.readfile()
        lines = analyze.get_lines(result)
        objects = analyze.get_objects(lines)
        self.assertEqual(20, len(objects))

    def test_get_distinct_outcomes(self):
        analyze = Analyze()
        result = analyze.readfile()
        lines = analyze.get_lines(result)
        objects = analyze.get_objects(lines)
        result = analyze.get_distinct_outcomes(objects)
        self.assertEqual(28, len(result))

    def test_get_age_groups(self):
        analyze = Analyze()
        result = analyze.readfile()
        lines = analyze.get_lines(result)
        objects = analyze.get_objects(lines)
        result = analyze.get_age_groups(objects)
        self.assertEqual(10, len(result))

    def test_get_outcomes_with_age(self):
        analyze = Analyze()
        result = analyze.readfile()
        lines = analyze.get_lines(result)
        objects = analyze.get_objects(lines)
        result = analyze.get_outcomes_with_age(objects)
        self.assertEqual(28, len(result))

    def test_plot(self):
        analyze = Analyze()
        result = analyze.readfile()
        lines = analyze.get_lines(result)
        objects = analyze.get_objects(lines)
        result = analyze.plot_subs(objects)



if __name__ == '__main__':
    unittest.main()