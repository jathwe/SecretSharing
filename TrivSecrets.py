import hashlib

def make_random_shares(numShares):
    secretString = "This is a trivial secret share implementation"
    secret = abs(hash(s))**10%100000000000000000000000000000000

    shares = [2,3,4]
    return secret, shares

def main():
    numShares = 6
    secret, shares = make_random_shares(numShares)
    print (secret)
    print (shares[1])


if __name__ == '__main__':
    main()