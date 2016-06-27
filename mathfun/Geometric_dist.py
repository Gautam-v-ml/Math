from scipy.stats import geom
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

class Geometric():

    def plot(self):
        p = 0.5
        mean, var, skew, kurt = geom.stats(p, moments='mvsk')


        x = np.arange(geom.ppf(0.01, p),
              geom.ppf(0.99, p))
        ax.plot(x, geom.pmf(x, p), 'bo', ms=8, label='geom pmf')
        ax.vlines(x, 0, geom.pmf(x, p), colors='b', lw=5, alpha=0.5)

        rv = geom(p)
        ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
                    label='frozen pmf')
        ax.legend(loc='best', frameon=False)
        plt.show()

    def pmf(self, x, p):
        pmf = geom.pmf(self, x, p)
        return pmf

    def cdf(self , x, p):
        cdf = geom.cdf(self, x, p)
        return cdf

    def entropy(self, p):
        ent = geom.entropy(self, p)
        return ent

    def mean(self, p):
        mu = geom.mean(self, p)
        return mu

    def median(self, p):
        med = geom.median(self, p)
        return med

    def var(self, p):
        var = geom.var(self, p)
        return var

    def std(self, p):
        std = geom.std(self, p)
        return std

