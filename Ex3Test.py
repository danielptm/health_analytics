import unittest
from Ex3 import Ex3
from sklearn.datasets import load_iris

class Ex3Test(unittest.TestCase):

    # def test_get_line_objects(self):
    #     ex3 = Ex3()
    #     line_objects = ex3.get_line_objects()
    #     self.assertEqual(55555, len(line_objects))

    def test_run_regression(self):
        ex = Ex3()
        ex.run_regression()
        # x, y = load_iris(return_X_y = True)
        # print(x)