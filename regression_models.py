import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

df = pd.read_csv("temp_data.csv")
#independant variable needs to be 2D, hence Dataframe
X = df[["time"]]
#dependant variable can be 1D, hence Series
Y = df["temperature"]

linear_model = LinearRegression()
poly = PolynomialFeatures(3)
X_Poly = poly.fit_transform(X)
poly_model = LinearRegression()
poly_model.fit(X_Poly, Y)
linear_model.fit(X,Y)
poly_predictions = poly_model.predict(X_Poly)
linear_predictions = linear_model.predict(X)

plt.scatter(df["time"],df["temperature"], label = "Original data")
plt.plot(df["time"],linear_predictions, color = "red", label = "Linear Predictions")
plt.plot(df["time"],poly_predictions, color = "green", label = "Polynomial Predictions")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.legend()
plt.title("Linear Regression: Temperature vs Time")
plt.show()