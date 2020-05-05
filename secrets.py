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