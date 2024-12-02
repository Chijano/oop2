from Decorators import timer


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


@timer
def find_primes():
    primes = []
    for num in range(2, 1001):
        if is_prime(num):
            primes.append(num)
    return primes


@timer
def find_primes2(start=2, end=1000):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes
