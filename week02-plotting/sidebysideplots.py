# Side by side plots
# Author : Michelle O'Connor

import matplotlib.pyplot as plt
import numpy as np

plt.subplot (1,2,1)
# 1 row, 2 columns, 1st plot in it
x = np.random.normal(0.0, 1.0, 10000)
plt.hist(x)

plt.subplot (1,2,2)
# 1 row, 2 columns, 2nd plot in it
x = np.random.uniform(-3.0, 3.0, 10000)
plt.hist(x)

plt.show()