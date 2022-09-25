# IM GOING TO KILL MYSELF
#!/usr/bin/python
import pandas as pd


# DRIVER CODE
df = pd.read_csv("rainfall.txt", sep=" ", header=None,
                 names=["City", "Rainfall Value"])

rf_mean = df['Rainfall Value'].mean() * 2.54  # finding mean
print("The mean rainfall value is:", rf_mean, "cm")
cities_mean = df["Rainfall Value"] > rf_mean
print(cities_mean)
