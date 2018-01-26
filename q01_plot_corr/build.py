# Default imports
import pandas as pd
from matplotlib.pyplot import yticks, xticks, subplots, set_cmap

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your solution here:
import matplotlib.pyplot as plt
import seaborn as sns
def plot_corr(data,size=11):
    plt.figure(figsize=(15,12))
    cmap = sns.diverging_palette(220, 20, as_cmap=True)
    sns.heatmap(data.corr(),cmap=cmap)
    plt.show()
