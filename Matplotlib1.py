#Problem 1 & 2
import matplotlib.pyplot as plt
 
x = [1,2,3,4,5] 
y = [1,4,9,16,25]
plt.plot(x,y)
plt.show()

x = [1,2,3,4,5] 
y = [1,4,9,16,25]
plt.bar(x,y)
plt.show()

y = [1,4,9,16,25]
plt.hist(y)
plt.show()

x = [1,2,3,4,5] 
y = [1,4,9,16,25]
plt.scatter(x, y)
plt.show()

x = [1,2,3,4,5] 
y = [1,4,9,16,25]
plt.plot(x,y,'o')
plt.show()

#problem 3
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 15)
cos = np.cos(x)
sin = np.sin(x)

ax = plt.axes([0.1, 0.1, 0.8, 0.8]) 

ax1 = ax.plot(x, cos, 'bs:') 

ax2 = ax.plot(x, sin, 'ro-') 
  
ax.legend(labels = ('Cosine Function', 
                    'Sine Function'), 
          loc = 'upper left')
  
ax.set_title("Trigonometric Functions")
  
plt.show()

#Problem 4
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 2.0, 0.01)
y = 1 + np.sin(2 * np.pi * x)

fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
ax1.plot(x, y, color="orange")
ax2.plot(x, y, color="green")
ax3.plot(x, y, color="blue")
ax4.plot(x, y, color="magenta")
ax5.plot(x, y, color="black")
ax6.plot(x, y, color="red")