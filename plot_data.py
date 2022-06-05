import data_loader
from matplotlib import pyplot as plt
import numpy as np

def plot(filename, *args):
    if len(filename)>0:
        data = data_loader.loadData(filename)
    else:
        data = data_loader.loadData()

    x_accel, y_accel, z_accel, t = data_loader.prepareData(data)
    if (len(args) > 0):
        mean = args[0]
        x_accel = x_accel - mean[0]
        y_accel = y_accel - mean[1]
    #size = x_accel.size
    #t = np.linspace(0, 100, num=size)

    plt.figure()
    plt.subplot(2,2,1)
    plt.plot(t, x_accel)
    plt.title("x_accel")
    plt.xlabel("t")
    plt.ylabel("a, m/s^2")
    plt.grid(True)

    plt.subplot(2,2,2)
    plt.plot(t, y_accel)
    plt.title("y_accel")
    plt.xlabel("t")
    plt.ylabel("a, m/s^2")
    plt.grid(True)

    plt.subplot(2, 2, 3)
    plt.plot(t, z_accel)
    plt.title("z_accel")
    plt.xlabel("t")
    plt.ylabel("a, m/s^2")
    plt.grid(True)

    plt.show()

#plot("data/accel_data_zero.csv")