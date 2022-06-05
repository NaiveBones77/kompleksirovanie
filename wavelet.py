from pywt import wavedec
import pywt
import data_loader
from pylab import *
from numpy import *

data = data_loader.loadData()
x_accel = data[:, 0]
size = x_accel.size
t = linspace(0, 100, num=size)

st = 'sym5'

coeffs = pywt.wavedec(x_accel, st, level=13)

#cD[300:] = 0
#cA[500:] = 0
recon = pywt.waverec(coeffs, 'sym5', )
#recon_a = pywt.upcoef('a', cA, 'sym5', 2) + pywt.upcoef('d', cD, 'sym5', 2)



subplot(2, 2, 1)
plot(x_accel,'b',linewidth=2, label='initial')
grid()
legend(loc='best')
subplot(2, 2, 2)
plot(recon,'r',linewidth=2, label='recon')
grid()
legend(loc='best')
show()