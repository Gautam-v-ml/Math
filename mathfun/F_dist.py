from scipy.stats import f
import matplotlib.pyplot as plt


class Gamma_Dist():

    def plot(self, x, n, p):
        pmf = f.pmf(x, n, p)
        plt.plot(x, pmf, 'o-')
        plt.title('F : n=%i , p=%.2f' % (n, p), fontsize='value')
        plt.xlabel('Number of successes')
        plt.ylable('Probability of Successes', fontsize='value')
        plt.show()

    def cdf(self, x, p):
        cdf = f.cdf(x, p)
        return cdf

    def pmf(self, x, n, p):
        pmf = f.pmf(x, n, p)
        return pmf

    def mean(self, n, p):
        mu = f.mean(self, n, p)
        return mu

    def median(self, n, p):
        med = f.median(self, n, p)
        return med

    def var(self, n, p):
        var = f.var(self, n, p)
        return var

    def std(self, n, p):
        std = f.std(self, n, p)
        return std

    def entropy(self, n, p):
        ent = f.entropy(self, n, p)
        return ent
