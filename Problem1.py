from matplotlib import pyplot as plt

x = [5, 2, 9, 4, 2]
y = [10, 5, 8, 4, 2]

# Plot
plt.plot(x,y)
# Show the plot
plt.show()

#Bar plot
plt.bar(x,y)
plt.show()

#Histogram plot
plt.hist(y)
plt.show()

#Scatter plot
plt.scatter(x,y)
plt.show()

#Scatter plot 
plt.plot(x,y,'o')
plt.show()
