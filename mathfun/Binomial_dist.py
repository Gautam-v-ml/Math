import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

'''
p = probability of sucesses
n = no. of independent trials
p(X = x)


'''
class Binomial():


    def prob_mass_fun(self, x , n, p):
        pmf = stats.binom.pmf(x , n, p)
        return pmf

    def plot(self , x, n, p):
        pmf = stats.binom.pmf(x , n, p)
        plt.plot(x, pmf, 'o-')
        plt.title('Binomial: n=%i , p=%.2f' % (n, p), fontsize='value')
        plt.xlabel('Number of successes')
        plt.ylable('Probability of Successes', fontsize='value')
        plt.show()


    def Cumulative_den_fun(self, x, p):
        cdf = stats.binom.cdf(x,p)
        return cdf


    def log_pmf(self , x, n, p):
        logpmf = stats.binom.logpmf(x , n, p)
        return logpmf


    def mean(self, n, p):
        mu = stats.binom.mean(self, n, p)
        return mu


    def median(self, n, p ):
        med = stats.binom.median(self, n, p)
        return med


    def var(self, n, p):
        var = stats.binom.var(self, n, p)
        return var

    def std(self, n, p):
        std = stats.binom.std(self, n, p)
        return std

