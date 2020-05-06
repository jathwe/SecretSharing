import hashlib
from random import randint

#definitions for ease of use
#a 33 digit max to use as mod so we get 32 digit integer
_max = 100000000000000000000000000000000

def make_random_shares(numShares):
    #long string to get a BIG hash
    secretString = "This is a trivial secret share implementation"
    secret = abs(hash(secretString))**10%_max

    shares = []
    
    accum = secret

    '''
    Subtract a random int from the secret
    Store that int as a share
    Repeat until num shares reached
    The remainer is the final share
    '''
    for i in range(numShares-1):
        share = randint(0,accum)
        shares.append(share)
        accum = accum-share
    shares.append(accum)

    return secret, shares
    
#simply sums all shares
def recover_secret(shares):
    return sum(shares)

def main():
    numShares = 6
    secret, shares = make_random_shares(numShares)
    print ('Secret:',secret)
    print ('Shares:')
    if shares:
        for share in shares:
            print(' ',share)
    print('Secret Recovered: ',recover_secret(shares))


if __name__ == '__main__':
    main()