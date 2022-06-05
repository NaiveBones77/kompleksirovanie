import numpy as np
import data_loader
import allan_variance as av
from allan_variance1 import allan_variance, params_from_avar
import commons
from matplotlib import pyplot as plt

 # CSV data file "gx,gy,gz"
fs = 54  # Sample rate [Hz]


    # Load CSV into np array
dataArr = data_loader.loadData("data/accel_data_zero130.csv")
ts = 1.0 / fs

    # Separate into arrays
gx = dataArr[:, 0]   # [deg/s]
gy = dataArr[:, 1]
gz = dataArr[:, 2]

IQR = commons.calculateIQR(gx)
    # Calculate gyro angles
thetax = np.cumsum(gx) * ts  # [deg]
thetay = np.cumsum(gy) * ts
thetaz = np.cumsum(gz) * ts

    # Compute Allan deviations
(taux, adx) = av.AllanDeviation(thetax, fs, maxNumM=100)
(tauy, ady) = av.AllanDeviation(thetay, fs, maxNumM=100)
(tauz, adz) = av.AllanDeviation(thetaz, fs, maxNumM=100)

tau, av = allan_variance(gz, ts, input_type='increment')
paramsx, av_predx = params_from_avar(tau, av)
print(paramsx)

    # Plot data on log-scale
plt.figure()
plt.title('Gyro Allan Deviations')
plt.plot(taux, adx, label='gx')
plt.plot(tauy, ady, label='gy')
plt.plot(tauz, adz, label='gz')
plt.xlabel(r'$\tau$ [sec]')
plt.ylabel('Deviation [deg/sec]')
plt.grid(True, which="both", ls="-", color='0.65')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.show()


