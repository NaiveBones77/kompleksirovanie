import os
import numpy as np

filename1 = "C:\\PycharmProjects\\accelormetr\data\\accel_test1.csv"
filename2 = "C:\\PycharmProjects\\accelormetr\data\\accel_test2.csv"
filename3 = "C:\\PycharmProjects\\accelormetr\data\\accel_zero2.csv"
filename4 = "C:\PycharmProjects\\accelormetr\data\\accel_upNdDown.csv"
filename5 = "C:\PycharmProjects\\accelormetr\data\\accel_rightLeft.csv"
filename6 = "C:\\PycharmProjects\\accelormetr\data\\accel-data_zero2.csv"

def loadData(filename = filename4):
    with open(filename) as f:
        pr = f.readlines()
        pr = pr[1:]
        pr = pr[:-1]
        data = []
        for elem in pr:
            data.append(np.float_(elem.split()))
        data = np.array(data)
        return data

def prepareData(data:np.ndarray):
    return (data[:, 0], data[:, 1], data[:, 2], data[:, 3])

def save_koeffs(array:np.ndarray, name, mode = 1):
    with open(name, 'wb') as f:
        np.save(f, array)

def load_koeffs(path, mode=1):
    with open(path, 'rb') as f:
        return np.load(f)

