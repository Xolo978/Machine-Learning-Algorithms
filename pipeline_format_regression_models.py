from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
import pandas as pd
# Create a polynomial regression model
degree = 12  # You can adjust the degree based on the data
polyreg_model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
df = pd.read_csv("temp_data.csv")
X = df[["time"]]
Y = df["temperature"]
# Fit the model
polyreg_model.fit(X, Y)

# Make predictions
poly_predictions = polyreg_model.predict(X)

# Plotting the results
plt.scatter(df["time"], df["temperature"], label="Original Data")  # Scatter plot of original data
plt.plot(df["time"], poly_predictions, color='red', label="Polynomial Regression Line")  # Polynomial regression line
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.legend()
plt.title("Polynomial Regression: Temperature vs Time")
plt.show()
