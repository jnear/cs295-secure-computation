# This code is adapted from:
# https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing

import functools
import random

_RINT = functools.partial(random.SystemRandom().randint, 0)

def _eval_at(poly, x, prime):
    """Evaluates polynomial (coefficient tuple) at x, used to generate a
    shamir pool in make_random_shares below.
    """
    accum = 0
    for coeff in reversed(poly):
        accum *= x
        accum += coeff
        accum %= prime
    return accum

def make_random_shares(minimum, shares, prime=_PRIME):
    """
    Generates a random shamir pool, returns the secret and the share
    points.
    """
    if minimum > shares:
        raise ValueError("Pool secret would be irrecoverable.")
    poly = [_RINT(prime - 1) for i in range(minimum)]
    points = [(i, _eval_at(poly, i, prime))
              for i in range(1, shares + 1)]
    return poly[0], points

def _extended_gcd(a, b):
    """
    Division in integers modulus p means finding the inverse of the
    denominator modulo p and then multiplying the numerator by this
    inverse (Note: inverse of A is B such that A*B % p == 1) this can
    be computed via extended Euclidean algorithm
    http://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Computation
    """
    x = 0
    last_x = 1
    y = 1
    last_y = 0
    while b != 0:
        quot = a // b
        a, b = b, a % b
        x, last_x = last_x - quot * x, x
        y, last_y = last_y - quot * y, y
    return last_x, last_y

def _divmod(num, den, p):
    """Compute num / den modulo prime p

    To explain what this means, the return value will be such that
    the following is true: den * _divmod(num, den, p) % p == num
    """
    inv, _ = _extended_gcd(den, p)
    return num * inv

def _lagrange_interpolate(x, x_s, y_s, p):
    """
    Find the y-value for the given x, given n (x, y) points;
    k points will define a polynomial of up to kth order.
    """
    k = len(x_s)
    assert k == len(set(x_s)), "points must be distinct"
    def PI(vals):  # upper-case PI -- product of inputs
        accum = 1
        for v in vals:
            accum *= v
        return accum
    nums = []  # avoid inexact division
    dens = []
    for i in range(k):
        others = list(x_s)
        cur = others.pop(i)
        nums.append(PI(x - o for o in others))
        dens.append(PI(cur - o for o in others))
    den = PI(dens)
    num = sum([_divmod(nums[i] * den * y_s[i] % p, dens[i], p)
               for i in range(k)])
    return (_divmod(num, den, p) + p) % p

def recover_secret(shares, prime=_PRIME):
    """
    Recover the secret from share points
    (x, y points on the polynomial).
    """
    if len(shares) < 2:
        raise ValueError("need at least two shares")
    x_s, y_s = zip(*shares)
    return _lagrange_interpolate(0, x_s, y_s, prime)

def share_input(inp, minimum, shares, prime=_PRIME):
    if minimum > shares:
        raise ValueError("Pool secret would be irrecoverable.")
    poly = [inp] + [_RINT(prime - 1) for i in range(minimum-1)]
    points = [(i, _eval_at(poly, i, prime))
              for i in range(1, shares + 1)]
    return points

# Finite field arithmetic (plus, mult, sum)

def plusFE(p, a, b):
    """Add field elements a and b in GF(p)"""
    return (a + b) % p

def multFE(p, a, b):
    """Multiply field elements a and b in GF(p)"""
    return (a * b) % p

def sumFE(p, xs):
    """Sum up a list of field elements xs in GF(p)"""
    total = 0
    for x in xs:
        total = plusFE(p, x, total)
    return total

# Share and reconstruct for Shamir sharing

def share_shamir(t, n, x, prime=_PRIME):
    shares_with_x = share_input(x, minimum=t, shares=n, prime=prime)
    return [y for x,y in shares_with_x]

def reconstruct_shamir(shares, prime=_PRIME):
    shares_with_x = list(zip(range(1, len(shares)+1), shares))
    return recover_secret(shares_with_x, prime=prime)

# Finite field matrix inversion, algorithm from here:
# https://stackoverflow.com/questions/4287721/easiest-way-to-perform-modular-matrix-inversion-with-python

def inversemodp(a, p):
    a = a % p
    if (a == 0):
        #print "a is 0 mod p"
        return None
    if a > 1 and p % a == 0:
        return None
    #(x,y) = generalizedEuclidianAlgorithm(p, a % p);
    (x,y) = _extended_gcd(p, a % p);
    inv = y % p
    assert (inv * a) % p == 1
    return inv

def identitymatrix(n):
    return [[int(x == y) for x in range(0, n)] for y in range(0, n)]

def inversematrix(matrix, q):
    n = len(matrix)
    A = np.matrix([[ matrix[j, i] for i in range(0,n)] for j in range(0, n)], dtype = int)
    Ainv = np.matrix(identitymatrix(n), dtype = int)
    for i in range(0, n):
        factor = inversemodp(A[i,i], q)
        if factor is None:
             raise ValueError("Error: no factor")
        A[i] = A[i] * factor % q
        Ainv[i] = Ainv[i] * factor % q
        for j in range(0, n):
            if (i != j):
                factor = A[j, i]
                A[j] = (A[j] - factor * A[i]) % q
                Ainv[j] = (Ainv[j] - factor * Ainv[i]) % q
    return Ainv
