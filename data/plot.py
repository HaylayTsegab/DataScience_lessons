#importing required libraries for data visualization
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import pandas as pd
# data name from the seaborn library
data = sns.load_dataset('tips')
#examining the fist five rows of the data
print(data.head())
#looking if there are missing valuse in the dataset
sns.heatmap(data.isnull(),yticklabels=False,cbar=False,cmap='viridis')
#plotting the data
sns.barplot(x='day',y='total_bill',data=data)
plt.show()