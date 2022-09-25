'''
Marian Remoroza
CS 2410 Data Science
Program 1: Python Control Structures, Functions, and Text File Processing
'''
#!/usr/bin/python
import pandas as pd
cm = 0
rainfall = open("rainfall.txt", "r")
rf_cm = open("rainfall_cm.txt", "w")
for line in rainfall:
    values = line.split()
    inches = float(values[1])
    cm = inches*2.54
    rf_cm.write(f"{values[0]} {cm}\n")
rainfall.close()
rf_cm.close()

df = pd.read_csv("rainfall_cm.txt", sep=" ", header=None,
                 names=["City", "Rainfall Value"])

df2 = pd.read_csv("rainfall.txt", sep=" ", header=None,
                  names=["City", "Rainfall Value in Inches"])
print(df2)
# highest rainfall
high_rf = df.max()
print("City with the highest rainfall:\n", high_rf)
# lowest rainfall
low_rf = df.min()
print("City with the least amount of rainfall:\n", low_rf)
# mean rainfall
rf_mean = df['Rainfall Value'].mean()
print("The mean rainfall value is:", rf_mean, "cm")
# number of cities with rainfall greater than the mean
