from scipy.stats import bernoulli
import matplotlib.pyplot as plt


class Bernaulli():

    def pmf(self, n, p):
        pmf = bernoulli.pmf(self, n, p)
        return pmf

    def cdf(self, n, p):
        cdf = bernoulli.cdf(self, n, p)
        return cdf

    def mean(self, n, p):
        mu = bernoulli.mean(self, n, p)
        return mu

    def median(self, n, p):
        med = bernoulli.median(self, n, p)
        return med

    def var(self, n, p):
        var = bernoulli.var(self, n, p)
        return var

    def std(self , n, p):
        std = bernoulli.std(self, n, p)
        return std

    def entropy(self, p):
        ent = bernoulli.entropy(self, p)
        return ent

    def plot(self, n, p, x):
        pmf = bernoulli.pmf(x, n, p)
        plt.plot(x, pmf, 'o-')
        plt.title('Bernaulli: n=%i , p=%.2f' % (n, p), fontsize='value')
        plt.xlabel('Number of successes')
        plt.ylable('Probability of Successes', fontsize='value')
        plt.show()

