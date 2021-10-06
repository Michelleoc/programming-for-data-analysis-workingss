# adding titles,legends and labels
# Author : Michelle O'Connor

# Link https://matplotlib.org/stable/tutorials/introductory/pyplot.html

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0, 0.1)
y = 3.0 * x + 1.0

noise = np.random.normal(0.0, 1.0, len(x))

plt.plot(x,y + noise, "r.", label="Actual")
plt.plot(x,y, "b-", label="Model") # y line

plt.title("Simple plot")
plt.xlabel("Weight")
plt.ylabel("Mass")
plt.legend()

# if you add a legend, you must have labels inserted on the plots

plt.show()