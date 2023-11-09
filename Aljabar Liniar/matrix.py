import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1, 4, 3],
             [2, 5, 4],
             [1, -3, -2]])

x = np.linalg.inv(a)
print(x)w