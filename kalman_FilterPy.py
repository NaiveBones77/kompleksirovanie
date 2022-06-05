from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
import numpy as np
import data_loader
from matplotlib import pyplot as plt

def filterAccel(data:np.ndarray, axis = [1], plot=True):

    len = data.shape
    xOpt = []
    dt = 1./54
    for i in range(len[1]-1):
        f = KalmanFilter(dim_x=3, dim_z=1)

        f.x = np.array([0., 0., 0.])
        if (i == 2):
            f.x = np.array([0., 0., -9.81])
        f.F = np.array([[1., 1.*dt, 0],
                        [0., 1., 1.*dt],
                        [0., 0., 1.]])

        f.H = np.array([[0., 0., 1.]])

        f.P = np.array([[100., 0., 0.],
                        [0., 100., 0.],
                        [0., 0., 0.01]])

        f.R = 15

        f.Q = Q_discrete_white_noise(dim=3, dt=0.1, var=0.13)

        x_accel = data[:, i]
        len = x_accel.size
        x_opt = []
        for i in range(len):
            z = x_accel[i]
            f.predict()
            f.update(z)
            x_opt.append(f.x)
            #x_opt[i][2] = x_opt[i][2] + 9.81
        x_opt = np.array(x_opt)
        xOpt.append(x_opt[:, 2])

    x_accel, y_accel, z_accel, t = data_loader.prepareData(data)

    fig, ax = plt.subplots(3,1)
    ax[0].plot(t, xOpt[0], 'b--', linewidth=1,  label ='filtered', )
    ax[0].plot(t, x_accel, 'r', linewidth=0.5, label='non-filtered')
    ax[0].grid(True, which="both", ls="-", color='0.65')
    ax[0].set_ylabel('a, m/s^2')
    ax[0].set_xlabel('time, s')
    ax[0].legend()

    #ax[1].subplot(3, 1, 2)
    ax[1].plot(t, xOpt[1], 'b--', linewidth=1, label='filtered', )
    ax[1].plot(t, y_accel, 'r', linewidth=0.5, label='non-filtered')
    ax[1].grid(True, which="both", ls="-", color='0.65')
    ax[1].set_ylabel('a, m/s^2')
    ax[1].set_xlabel('time, s')
    ax[1].legend()

    #ax[1].subplot(3, 1, 3)
    ax[2].plot(t, xOpt[2], 'b--', linewidth=1, label='filtered', )
    ax[2].plot(t, z_accel, 'r', linewidth=0.5, label='non-filtered')
    ax[2].grid(True, which="both", ls="-", color='0.65')
    ax[2].set_ylabel('a, m/s^2')
    ax[2].set_xlabel('time, s')
    ax[2].legend()
    #ax[1].show()
    plt.show()
