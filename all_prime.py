"""all primes"""
def count_prime():
    """count prime"""
    n = int(input())
    prime_count = 0
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if not i % j:
                is_prime = False
                break
        if is_prime:
            prime_count += 1
    print(prime_count)
count_prime()
