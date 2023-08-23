from matplotlib import pyplot as plt

x = [1, 4, 3, 2, 8]
y = [6, 3, 7, 2, 4]

# Plot
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
# Show the plot
plt.show()

#Bar plot
plt.bar(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#Histogram plot
plt.hist(y)
plt.ylabel("y")
plt.show()

#Scatter plot
plt.scatter(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#Scatter plot 
plt.plot(x,y,'o')
plt.xlabel("x")
plt.ylabel("y")
plt.show()