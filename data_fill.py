import pandas as pd
import numpy as np
loaded_data = pd.read_csv("temp_data.csv")
# print(loaded_data)
# print(loaded_data.loc[5:10, "temperature"])

loaded_data.loc[5:10, "temperature"] = np.nan
# loaded_data["temperature"].fillna(loaded_data["temperature"].mean(), inplace=True)
#handling missing data
loaded_data.dropna(inplace=True)
print(loaded_data.head(15))