def generate_nth_primes(n):
    primes = [2]

    i = 3
    while len(primes) < n:
        isPrime = True
        for p in primes:
            if i % p == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(i)

        i += 2 # skip every even number

    return primes


if __name__ == "__main__":
    print(generate_nth_primes(10001)[-1:][0])
