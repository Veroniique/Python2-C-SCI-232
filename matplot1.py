#Apple and Microsoft stock chart over the years
import matplotlib.pyplot as plt

#sizing the figure
plt.figure(figsize=(10,6))

#list values
Apple = [0.80, 0.23, 0.35, 2.53, 3.28, 7.55, 17.30, 22.76, 23.95, 39.55, 73.41, 124.79, 180.40]
Microsoft = [28.53, 21.30, 27.71, 22.07, 19.25, 25.46, 27.62, 38.01, 51.17, 101.57, 157.70, 247.65, 269.63]
years = [2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024]

#plotting values on x and y from list
plt.plot(years, Apple, color="b", linestyle="--", marker=".", label="Apple")

#overlaying Microsoft on the graph
plt.plot(years, Microsoft, color="g", label="Microsoft")

#adding ticks
plt.xticks(range(2000, 2024 + 1, 2))
plt.yticks(range(0, int(max(Microsoft)) + 25, 25))

#adding labels
plt.title("Apple and Microsoft stock prices over the years")
plt.ylabel("Price ($)")
plt.xlabel("Years")

#showing plot and adding labels
plt.legend()
plt.show()