from math import gcd

N = 11413
e = 19
C = [3203, 909, 3143, 5255, 5343, 3203, 909, 9958, 5278, 5343, 9958,
     5278, 4674, 909, 9958, 792, 909, 4132, 3143, 9958, 3203, 5343, 792, 3143, 4443]


def phi(n):
    amount = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            amount += 1
    return amount


d = pow(e, -1, phi(N))

result = ''
for y in C:
    result += (chr(y ** d % N))

print(result)
