import matplotlib.pyplot as plt

#list values
house = [5000, 11000, 17000, 25000, 40000, 26000, 30000, 35000, 60000, 70000, 100000, 150000, 200000]
housetwo = [6000, 15000, 19000, 20000, 30000, 15000, 35000, 45000, 80000, 70000, 100000, 180000, 190000]
years = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]

#plotting values on x and y from list
plt.plot(years, house, color="b",linestyle="--", marker=".")

#overlay the housetwo into the graph
plt.plot(years, housetwo, color="g")

#adding labels
plt.title("House Prices")
plt.ylabel("House Prices in dollars")
plt.xlabel("Prices")

plt.show()



