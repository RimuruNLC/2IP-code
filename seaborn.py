import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="ticks")
plt.figure(figsize=(10, 6))
tablica = pd.read_csv("winequality-white.csv", sep=";")
sns.scatterplot(tablica)
plt.show()
