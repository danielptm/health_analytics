from typing import List
import matplotlib.pyplot as plt
from model.Ex3Line import Ex3Line
from model.DataPoint import DataPoint
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt

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
        howmany = []
        for line in lines:
            items = line.split(",")
            if items[0] not in howmany:
                howmany.append(items[0])
            line_object = Ex3Line(items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7])
            self.line_objects.append(line_object)



    def run_regression(self):
        df = pd.read_csv('resources/ex3_t.csv')

        # defining the dependent and independent variables
        Xtrain = df['state']
        ytrain = df['overall_outcome']
        x2 = pd.get_dummies(Xtrain)

        log_reg = sm.Logit(ytrain.astype(int), x2).fit()

        print(log_reg.summary())

    def calculate_stuff(self):
        lines = []
        odds = []
        probabilities = []
        with open('resources/betas.csv', 'r') as file:
            data = file.read()
        lines = data.splitlines()

        res = ''
        for line in lines:
            items = line.split(",")
            state = items[0]
            beta = float(items[1])
            o = np.exp(beta)
            prob = o / (1 + o)
            res += state + "," + str(beta) + "," + str(o) + "," + str(prob) + '\n'

        print(res)
        return None

    def show_table(self):
        fig, ax = plt.subplots()

        # hide the axes
        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')

        df = pd.read_csv("resources/final.csv")
        table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')

        # display table
        plt.show()




