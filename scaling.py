import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, Normalizer
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("temp_data.csv")

# Standardization
scaler_s = StandardScaler()
# Two brackets so that it loads the temperature data as a DataFrame and not Series, since fit_transform accepts 2D
df["temperature_scaled_s"] = scaler_s.fit_transform(df[["temperature"]])

# Normalization
scaler_n = Normalizer()
df["temperature_scaled_n"] = scaler_n.fit_transform(df[["temperature"]])

# Plotting
plt.plot(df["time"], df["temperature"], label="Original temp")
plt.plot(df["time"], df["temperature_scaled_s"], label="Standardized temp", color="red")
plt.plot(df["time"], df["temperature_scaled_n"], label="Normalized temp", color="green")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.legend()
plt.show()