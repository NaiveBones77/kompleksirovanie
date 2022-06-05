import numpy as np
from matplotlib import pyplot as plt

N = 100
a = 0.1
sigmaPsi = 5
sigmaEta = 100
k = np.linspace(1, N, N)
x = k
x[0] = 0
z = np.zeros_like(x)
z[0] = x[0] + np.random.normal(0, sigmaPsi)

for t in range(N-1):
    x[t+1] = x[t] + a*t + np.random.normal(0, sigmaPsi)
    z[t+1] = x[t+1] + np.random.normal(0, sigmaPsi)

plt.subplot(2,2,1)
plt.plot(k, x)
plt.subplot(2,2,2)
plt.plot(k, z)


xOpt = np.zeros_like(x)
xOpt[0]=z[0]
eOpt = np.zeros_like(x)
eOpt[0] = sigmaEta
K = np.zeros_like(x)
K[0] = 0.7

for t in range(N-1):
    eOpt[t+1] = np.sqrt((sigmaEta**2)*(eOpt[t]**2+sigmaPsi**2)/(sigmaEta**2+eOpt[t]**2+sigmaPsi**2))
    K[t+1] = (eOpt[t+1])**2/sigmaEta**2
    xOpt[t+1] = (xOpt[t]+a*t)*(1-K[t+1]) + K[t+1]*z[t+1]

plt.subplot(2,2,3)
plt.plot(k,xOpt)
plt.show()

    