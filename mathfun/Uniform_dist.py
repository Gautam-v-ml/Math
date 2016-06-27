import matplotlib.pyplot as plt
import numpy as np
import math


class Uniform_Dist():
    def plot(a, b, c):
        s = np.random.uniform(a, b, c)
        count, bins, ignored = plt.hist(s, 15, normed=True)
        plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
        plt.show()

    def mean(a, b):
        mu = float(1.0/(b + a))
        return mu

    def median(a, b):
        med = float((a + b) / 2.0)
        return med

    def varience(a, b):
        x= (b - a)*(b - a)
        sigma = (1.0/12.0)*x
        return sigma

    def entropy(a, b):
        en = math.log(b - a)
        return en

    def sekwness(self):
        skewness = 0
        return skewness

    def moment_gen_fun(a, b, t):
        if(t == 0):
            mgf = 1
            return mgf

        else:
            x =float( math.exp(t*b) - math.exp(t*a))
            y = float(t*(b - a))
            mgf = float(x / y)
            return mgf


