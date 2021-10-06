# pylot testing
# Author : Michelle O'Connor

# Link https://matplotlib.org/stable/tutorials/introductory/pyplot.html

# [] for list
# no x numbers given
# plt.plot([1, 2, 3, 4])
# enter this way to give both x and y, the first set are x values and second set are the y values 
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "b.")
plt.ylabel('Some numbers')
plt.xlabel('More numbers')
plt.show()

# b. blue dots instead of lines