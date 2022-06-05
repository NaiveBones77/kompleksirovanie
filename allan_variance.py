import numpy as np

def AllanDeviation(dataArr: np.ndarray, fs: float, maxNumM: int=100):
    ts = 1.0 / fs
    N = len(dataArr)
    Mmax = 2 ** np.floor(np.log2(N / 2))
    M = np.logspace(np.log10(1), np.log10(Mmax), num=maxNumM)
    M = np.ceil(M)  # Round up to integer
    M = np.unique(M)  # Remove duplicates
    taus = M * ts  # Compute 'cluster durations' tau

    # Compute Allan variance
    allanVar = np.zeros(len(M))
    for i, mi in enumerate(M):
        twoMi = int(2 * mi)
        mi = int(mi)
        allanVar[i] = np.sum(
            (dataArr[twoMi:N] - (2.0 * dataArr[mi:N - mi]) + dataArr[0:N - twoMi]) ** 2
        )

    allanVar /= (2.0 * taus ** 2) * (N - (2.0 * M))
    return (taus, np.sqrt(allanVar))