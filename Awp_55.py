import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(size=1000)
y = np.random.normal(size=1000)
plt.hexbin(x, y, gridsize=50, cmap='Greens')
plt.colorbar()
plt.show()
