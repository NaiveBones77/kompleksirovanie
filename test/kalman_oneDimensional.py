import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt

xs = range(500)
ys = randn(500)*1. + 10.
plt.plot(xs, ys)

print(f'Mean of readings is {np.mean(ys):.3f}')
plt.show()