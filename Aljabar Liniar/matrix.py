import numpy as np

a = np.array([[1, 4, 3],
             [2, 5, 4],
             [1, -3, -2]])

x = numpy.linalg.inv(a)
print(x)