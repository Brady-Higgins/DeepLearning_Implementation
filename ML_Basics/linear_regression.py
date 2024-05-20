import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as ax
from matplotlib.animation import FuncAnimation


class LinearRegression:
    def __init__(self):
        self.parameters = {}
    def forward_propogation(self, train_input):
        m = self.parameters['m']
        c = self.parameters['c']
        predictions = np.multiply(m,train_input) + c
        return predictions
    