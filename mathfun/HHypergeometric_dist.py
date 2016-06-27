from scipy.stats import hypergeom
import matplotlib.pyplot as plt

class Hypergeo():

    def plot(self, x, n, p):
        pmf = hypergeom.pmf(x, n, p)
        plt.plot(x, pmf, 'o-')
        plt.title('HyperGeometric: n=%i , p=%.2f' % (n, p), fontsize='value')
        plt.xlabel('Number of successes')
        plt.ylable('Probability of Successes', fontsize='value')
        plt.show()

    def Cumulative_den_fun(self, x, p):
        cdf = hypergeom.cdf(x, p)
        return cdf

    def log_pmf(self, x, n, p):
        logpmf = hypergeom.logpmf(x, n, p)
        return logpmf

    def mean(self, n, p):
        mu = hypergeom.mean(self, n, p)
        return mu

    def median(self, n, p):
        med = hypergeom.median(self, n, p)
        return med

    def var(self, n, p):
        var = hypergeom.var(self, n, p)
        return var

    def std(self, n, p):
        std = hypergeom.std(self, n, p)
        return std

    def entropy(self, n, p):
        ent = hypergeom.entropy(self, n, p)
        return ent
