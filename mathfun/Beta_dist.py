from scipy.stats import beta
import matplotlib.pyplot as plt


class Gamma_Dist():

    def plot(self, x, n, p):
        pmf = beta.pmf(x, n, p)
        plt.plot(x, pmf, 'o-')
        plt.title('Beta: n=%i , p=%.2f' % (n, p), fontsize='value')
        plt.xlabel('Number of successes')
        plt.ylable('Probability of Successes', fontsize='value')
        plt.show()

    def cdf(self, x, p):
        cdf = beta.cdf(x, p)
        return cdf

    def pmf(self, x, n, p):
        pmf = beta.pmf(x, n, p)
        return pmf

    def mean(self, n, p):
        mu = beta.mean(self, n, p)
        return mu

    def median(self, n, p):
        med = beta.median(self, n, p)
        return med

    def var(self, n, p):
        var = beta.var(self, n, p)
        return var

    def std(self, n, p):
        std = beta.std(self, n, p)
        return std

    def entropy(self, n, p):
        ent = beta.entropy(self, n, p)
        return ent
