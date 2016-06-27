from scipy.stats import expon
import matplotlib.pyplot as plt


class Gamma_Dist():

    def plot(self, x, n, p):
        pmf = expon.pmf(x, n, p)
        plt.plot(x, pmf, 'o-')
        plt.title('Exoponetial: n=%i , p=%.2f' % (n, p), fontsize='value')
        plt.xlabel('Number of successes')
        plt.ylable('Probability of Successes', fontsize='value')
        plt.show()

    def cdf(self, x, p):
        cdf = expon.cdf(x, p)
        return cdf

    def pmf(self, x, n, p):
        pmf = expon.pmf(x, n, p)
        return pmf

    def mean(self, n, p):
        mu = expon.mean(self, n, p)
        return mu

    def median(self, n, p):
        med = expon.median(self, n, p)
        return med

    def var(self, n, p):
        var = expon.var(self, n, p)
        return var

    def std(self, n, p):
        std = expon.std(self, n, p)
        return std

    def entropy(self, n, p):
        ent = expon.entropy(self, n, p)
        return ent
