from scipy.stats import gamma
import matplotlib.pyplot as plt


class Gamma_Dist():
    def plot(self, x, n, p):
        pmf = gamma.pmf(x, n, p)
        plt.plot(x, pmf, 'o-')
        plt.title('Gamma: n=%i , p=%.2f' % (n, p), fontsize='value')
        plt.xlabel('Number of successes')
        plt.ylable('Probability of Successes', fontsize='value')
        plt.show()

    def Cumulative_den_fun(self, x, p):
        cdf = gamma.cdf(x, p)
        return cdf

    def log_pmf(self, x, n, p):
        logpmf = gamma.logpmf(x, n, p)
        return logpmf

    def mean(self, n, p):
        mu = gamma.mean(self, n, p)
        return mu

    def median(self, n, p):
        med = gamma.median(self, n, p)
        return med

    def var(self, n, p):
        var = gamma.var(self, n, p)
        return var

    def std(self, n, p):
        std = gamma.std(self, n, p)
        return std

    def entropy(self, n, p):
        ent = gamma.entropy(self, n, p)
        return ent
