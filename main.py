import numpy as np
import kalman_FilterPy
import data_loader
import commons
import plot_data


data = data_loader.loadData('data/accel_data_zero.csv')
commons.calc_bias_error("data/accel_data_zero.csv", "data/accel_data_zero2.csv")
mean = data_loader.load_koeffs('bias_error.np')
data = commons.supply_bias_error(data, mean)
plot_data.plot('data/accel_data_zero.csv', mean)

kalman_FilterPy.filterAccel(data, [1])