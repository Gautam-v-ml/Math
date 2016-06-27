from scipy.stats import poisson
import matplotlib.pyplot as plt

class Hypergeo():

    def plot(self, x, n, p):
        pmf = poisson.pmf(x, n, p)
        plt.plot(x, pmf, 'o-')
        plt.title('Poisson: n=%i , p=%.2f' % (n, p), fontsize='value')
        plt.xlabel('Number of successes')
        plt.ylable('Probability of Successes', fontsize='value')
        plt.show()

    def Cumulative_den_fun(self, x, p):
        cdf = poisson.cdf(x, p)
        return cdf

    def log_pmf(self, x, n, p):
        logpmf = poisson.logpmf(x, n, p)
        return logpmf

    def mean(self, n, p):
        mu = poisson.mean(self, n, p)
        return mu

    def median(self, n, p):
        med = poisson.median(self, n, p)
        return med

    def var(self, n, p):
        var = poisson.var(self, n, p)
        return var

    def std(self, n, p):
        std = poisson.std(self, n, p)
        return std

    def entropy(self, n, p):
        ent = poisson.entropy(self, n, p)
        return ent
