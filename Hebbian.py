import numpy as np

def theta(t1, t2):
    return 1 if t1 == t2 else 0

def hebbian(W, X, sigma, tau1, tau2, d):
    k, n = W.shape
    for (i, j), _ in np.ndenumerate(W):
        W[i, j] += X[i, j] * tau1 * theta(sigma[i], tau1) * theta(tau1, tau2)
        W[i, j] = np.clip(W[i, j] , -d, d)
        print('Wgüncel=',W)
        print('tau1=',tau1) 
        print('tau2=',tau2)
