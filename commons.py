import numpy as np
import data_loader

class Accelerometr():
    data = []

    def load_from_file(self, path):
        self.data = data_loader.loadData(path)

    def __init__(self, path):
        self.data = data_loader.loadData(path)

    def __init__(self):
        pass





def calculateIQR(data: np.ndarray):
    sort = np.sort(data)
    size = sort.size
    idx_meadian = int(sort.size / 2)
    Q1 = sort[int(idx_meadian/2)]
    Q3 = sort[int(idx_meadian/2 + idx_meadian)]
    return Q3-Q1

def calc_bias_error(path1, path2):
    data1 = data_loader.loadData(path1)
    data2 = data_loader.loadData(path2)
    mean1 = np.median(data1, axis=0)
    mean1 = mean1[:3]
    mean2 = np.median(data2, axis=0)
    mean2 = mean2[:3]
    mean = (mean1 + mean2) / 2
    data_loader.save_koeffs(mean, 'bias_error.np')

def supply_bias_error(data:np.ndarray, mean):
    res = data
    res[:,0] = res[:, 0] - mean[0]
    res[:,1] = res[:, 1] - mean[1]
    return res


