import matplotlib.pyplot as plt
import numpy as np

# 1D array of subplots
#Subplots returns a tuple of ndarray. Here it is a tuple of 1d array
x = [3, 1, 2]
y = [2, 5, 0]
z = [3, 2, 1]

fig, ax = plt.subplots(2)

ax[0].plot(y, x)
ax[1].plot(x, z)

plt.show()


# 2D array subplots

x = np.arange(0.0, 2.0, 0.01)
y = 1 + np.sin(2 * np.pi * x)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.plot(x, y, color="orange")
ax3.plot(x, y, color="blue")
ax4.plot(x, y, color="magenta")
ax2.plot(x, y, color="red")

plt.show()