import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('2017_2020.csv')
f, ax = plt.subplots(figsize=(14, 10))


corr = data.corr()
sns.heatmap(corr, cmap='RdBu', linewidths=0.05, ax=ax)
ax.set_title('Correlation between features')
plt.show()