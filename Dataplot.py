"""
Exploratory Data Analysis Plot
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-whitegrid')

class Dataplot:
    def __init__(self, data):
        self.data = data

    def count_plot(self, col, title, savefig=False):
        fig, ax = plt.subplots(figsize=(5, 4))
        countplot = sns.countplot(x=col, data=data, ax=ax)
        plt.title(f"{col} Columns")
        for container in countplot.containers:
            plt.bar_label(container)
        if savefig:
            plt.savefig(f"{col}_count_plot.png")
        plt.show()