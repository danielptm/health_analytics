from typing import List
import matplotlib.pyplot as plt
from model.Ex3Line import Ex3Line
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

class Ex3:

    data = None
    line_objects = []

    def __init__(self):
        self.readfile()
        self.load_line_objects()

    def readfile(self):
        with open('resources/ex3.csv', 'r') as file:
            data = file.read()
        self.data = data

    def load_line_objects(self):
        lines = self.data.splitlines()
        for line in lines:
            items = line.split(",")
            line_object = Ex3Line(items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7])
            self.line_objects.append(line_object)



    def run_regression(self):
        x = []
        y = []
        for item in self.line_objects:
            if item.state != "state":
                x.append(item.state)
                if item.overall_outcome == "Negative":
                    y.append(0)
                else:
                    y.append(1)
        label_encoder = LabelEncoder()
        x_num = label_encoder.fit_transform(x)

        np_x = np.asarray(x_num)
        np_y = np.asarray(y)

        clf = LogisticRegression().fit(np_x.reshape(-1,1), np_y)
        z = clf.score(np_x.reshape(-1,1), np_y)
        print(z)
