# Historgrams
# Author : Michelle O'Connor

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0.0, 1.0, 1000)
# loc, scale, size

plt.hist(x, bins=20)
# you can specify the number of bins

plt.show()

# columns on the bar chart are known as bins
# shows how many occurances there are for each bin