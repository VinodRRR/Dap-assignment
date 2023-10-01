import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("pwsupply.csv")
dataframe = pd.DataFrame(data)
dfh = dataframe.head(20)
dfh.plot(x="State_UTs_Name", y="hours",
         kind="bar", title="Power supply in Indian States in hours")
plt.show()