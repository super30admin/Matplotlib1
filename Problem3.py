import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
# left, bottom, width, height space from window
ax = plt.axes([0.1, 0.1, 0.7, 0.2])
plt.show()


fig = plt.figure()
ax = fig.add_axes([0.5, 0.4, 0.8, 0.9])
plt.show()


fig = plt.figure()
#[left, bottom, width, height]
ax = plt.axes([0.1, 0.1, 0.8, 0.8])

ax.legend(labels = ('label1', 'label2'),
		loc = 'upper left')
plt.show()


#Plotting sine and cosine functions and adding legend, title
X = np.linspace(-np.pi, np.pi, 15)
C = np.cos(X)
S = np.sin(X)

ax = plt.axes([0.1, 0.1, 0.8, 0.8])

ax1 = ax.plot(X, C, 'bH:')
ax2 = ax.plot(X, S, 'rD-')

ax.legend(labels = ('Cos Function', 'Sin Function'), loc = 'lower right')
ax.set_title("Trigonometric Functions")
ax.set_xlabel("x")
plt.show()
