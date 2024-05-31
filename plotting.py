import matplotlib.pyplot as plt

#value ranges for graph
x = list(range(0,10))
y = list(range(-10,0))

plt.plot(x,y)
#title of graph
plt.title("This is my sample of using matplotlib")

#labeling the x and y axis
plt.xlabel("X axis")
plt.ylabel("Y axis")

#changing the tick styles
plt.xticks((0,2,4,6,8), ("u","s","m","a","n"))

plt.show()
