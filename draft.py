'''
NOTE:
This is all the other codes I tried. I realized I didn't
add any comments on my final program run, so I just compiled all of my work here. '''

'''
Marian Remoroza
CS 2410 Data Science
Program 1: Python Control Structures, Functions, and Text File Processing
'''
#!/usr/bin/python

import pandas as pd
cm = 0
rainfall = open("rainfall.txt", "r")  # opening rainfall.txt
rf_cm = open("rainfall_cm.txt", "w")  # new file for cm values

for line in rainfall:  # converting rainfall.txt values to cm and then writing it to a new file
    values = line.split()
    inches = float(values[1])
    cm = inches*2.54  # conversion
    rf_cm.write(f"{values[0]} {cm}\n")
rainfall.close()
rf_cm.close()

df = pd.read_csv("rainfall_cm.txt", sep=" ", header=None,
                 names=["City", "Rainfall Value"])  # OG rainfall file

df2 = pd.read_csv("rainfall.txt", sep=" ", header=None,
                  names=["City", "Rainfall Value (in)"])  # rainfall file to use for output

print(df2)

high_rf = df.loc[df["Rainfall Value"].idxmax()]  # highest rainfall
print("City with the most amount of rainfall:\n", high_rf)

low_rf = df.min()   # lowest rainfall
print("City with the least amount of rainfall:\n", low_rf)

rf_mean = df['Rainfall Value'].mean()   # mean rainfall
rf = "{:.2f}".format(rf_mean)
print("The mean rainfall value is:", rf, "cm")

# number of cities with rainfall greater than the mean
# count values in one column w/ condition: len(df[df['Rainfall Value']==])
# print("There are ", , " of cities greater than the mean rainfall value.")
