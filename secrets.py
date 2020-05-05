from __future__ import division
from __future__ import print_function

import random
import functools

# Here we can declare whatever prime number we want, 
# this will determine the size of the key,
# the larger the prime, the larger the key
_PRIME = 2 ** 79 - 1

#random int to help keep things random
_RINT = functools.partial(random.SystemRandom().randint, 0)

def _eval_at(poly, x, prime):
    """
    A fancy function that makes the coefficient tuple at x, this 
    makes us our shamir pool in the def below.
    """
    accum = 0
    for coeff in reversed(poly):
        accum *= x
        accum += coeff
        accum %= prime
    return accum

def make_random_shares(minimum, shares, prime=_PRIME):
    """
    This makes whats called a shamir pool, the polynomial with
    the minimum being used and its shares shares
    """
    #some quick error checking so you dont make the minimum impossible to achieve
    if minimum > shares:
        raise ValueError("Pool secret would be irrecoverable.")
    poly = [_RINT(prime - 1) for i in range(minimum)]
    points = [(i, _eval_at(poly, i, prime))
              for i in range(1, shares + 1)]
    return poly[0], points

def main():
    #Make the secret and its shares
    secret, shares = make_random_shares(minimum=4, shares=8)

    #printing the secret and shares for demonstration.
    print('Secret:                                                     ',
          secret)
    print('Shares:')
    if shares:
        for share in shares:
            print('  ', share)

    #print the recoveries
    print('Secret recovered from minimum subset of shares:             ',
          recover_secret(shares[:4]))
    print('Secret recovered from a different minimum subset of shares: ',
          recover_secret(shares[-4:]))

if __name__ == '__main__':
    main()