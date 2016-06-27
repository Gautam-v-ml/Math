def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def num_combinations(n, k, with_replacement=False):

    if with_replacement:
        numerator = factorial(n + k - 1)
        denominator = factorial(k) * factorial(n-1)
    else:
        numerator = factorial(n)
        denominator = factorial(k) * factorial(n-k)
    comb = int(numerator/denominator)
    return comb


def num_permutations(n, k, with_replacement=False):

    if with_replacement:
        permut = n**k
    else:
        numerator = factorial(n)
        denominator = factorial(n-k)
        permut = int(numerator/denominator)
    return permut


