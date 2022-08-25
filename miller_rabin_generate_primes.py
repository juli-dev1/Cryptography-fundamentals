import random
import time
from gmpy2 import powmod


def miller_rabin(n, k):
    i = 1
    j = 0
    s, t = 0, n - 1
    while s % 2 == 0:
        s += 1
        t //= 2
    while i <= k:
        a = random.randrange(2, n - 1)
        b = powmod(int(a), int(t), int(n))
        if b == 1 or b == n - 1:
            j = j + 1
            if j == k:
                return True
        for r in range(0, s):
            if b == n - 1:
                j = j + 1
                if j == k:
                    return True
            b = powmod(b, 2, n)
        i += 1
    return False


def generate_prime(b=2048, k=1):
    while True:
        p = random.getrandbits(b)
        q = 2 * p + 1
        if miller_rabin(p, k) and miller_rabin(q, k):
            print('Strong probable primes')
            print('p = ' + str(p))
            print('q = ' + str(q))
            return p, q


start = time.time()
print('Start')
a, b = generate_prime()
end = time.time()
print(end - start)
