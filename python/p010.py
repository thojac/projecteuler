import numpy as np

def find_primes_sieve(n):
    isPrime = np.ones(n) # Every value in list marked as prime number
    isPrime[1] = 0 # mark 1 as not prime
    currPrime = 2
    while currPrime:
        isPrime[::currPrime] = 0 # Mark multiples of isPrimes as not prime
        isPrime[currPrime] = 1 # mas currPrime as it again... hehehe (
        currPrime = nextPrime(isPrime, currPrime)

    return isPrime.nonzero()[0]

def nextPrime(arr, pos):
    try:
        return np.where(arr[pos+1:] == 1)[0][0] + pos+1
    except IndexError:
        return 0


if __name__ == "__main__":
    res = find_primes_sieve(100)
    print(res)
    print(np.sum(res))
