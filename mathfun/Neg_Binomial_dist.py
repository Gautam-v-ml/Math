from scipy.stats import nbinom
import matplotlib.pyplot as plt


class N_Binomial():

    def prob_mass_fun(self, x , n, p):
        pmf = nbinom.pmf(x, n, p)
        return pmf

    def plot(self, x, n, p):
        pmf = nbinom.pmf(x, n, p)
        plt.plot(x, pmf, 'o-')
        plt.title('Neg_Binomial: n=%i , p=%.2f' % (n, p), fontsize='value')
        plt.xlabel('Number of successes')
        plt.ylable('Probability of Successes', fontsize='value')
        plt.show()

    def Cumulative_den_fun(self, x, p):
        cdf = nbinom.cdf(x,p)
        return cdf

    def log_pmf(self , x, n, p):
        logpmf = nbinom.logpmf(x , n, p)
        return logpmf

    def mean(self, n, p):
        mu = nbinom.mean(self, n, p)
        return mu

    def median(self, n, p ):
        med = nbinom.median(self, n, p)
        return med

    def var(self, n, p):
        var =nbinom.var(self, n, p)
        return var

    def std(self, n, p):
        std = nbinom.std(self, n, p)
        return std

    def entropy(self, n, p):
        ent = nbinom.entropy(self, n, p )
        return ent

