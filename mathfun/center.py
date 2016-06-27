import numpy as np
import scipy.stats as sp


def mean(X):
    mu = np.mean(X)
    return mu


def median(X):
    med = np.median(X)
    return med


def mode(X):
    mode = sp.mode(X)
    return mode


def std(X):
    sigma = np.std(X)
    return sigma


def var(X):
    var = np.var(X)
    return var
