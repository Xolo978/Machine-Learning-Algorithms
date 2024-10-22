import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    "time": np.linspace(0, 10, 100),
    "temperature": 20 + 10 * np.sin(np.linspace(0, 10, 100))
}
df = pd.DataFrame(data)
df.to_csv("temp_data.csv", index=False)
# loaded_data = pd.read_csv("temp_data.csv")
plt.plot(df["time"],df["temperature"], label="Temp vs time")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.legend()
plt.show()

