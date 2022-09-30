# IM GOING TO KILL MYSELF
#!/usr/bin/python

def high_rf(cities, rainfall):
    high = rainfall[0]
    high_city = cities[0]
    for i in range(len(cities)):
        if rainfall[i] > high:
            high = rainfall[i]
            high_city = cities[i]
    return (high_city, high)


def low_rf(cities, rainfall):
    low = rainfall[0]
    low_city = cities[0]
    for i in range(len(cities)):
        if rainfall[i] < low:
            low = rainfall[i]
            low_city = cities[i]
    return (low_city, low)


def mean_rf(rainfall):
    x = 0
    for i in range(len(rainfall)):
        x += rainfall[i]
    return (x/len(rainfall))


def above_mean(cities, rainfall, mean_rf):
    count = 0
    print("Cities above the mean rainfall:\n")
    for i in range(len(rainfall)):
        if mean_rf < rainfall[i]:
            print(cities[i], rainfall[i])


def main():
    cities = []
    rainfall_value = []
    fo = open("rainfall.txt", "r")
    read = fo.readlines()
    for line in read:
        city, rf = line.split(" ")
        cities.append(city)
        rainfall_value.append(float(rf)*2.54)

    print("City with the most amount of rainfall:",
          high_rf(cities, rainfall_value), "\n")
    print("City with the least amount of rainfall:", low_rf(
        cities, rainfall_value), "\n")
    m = mean_rf(rainfall_value)
    f = "{:.2f}".format(m)
    print("The mean rainfall value is:", f, "cm")
    above_mean(cities, rainfall_value, m)


main()
