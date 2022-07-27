def trial_division(n):
    L = []
    while n % 2 == 0:
        L.append(2)
        n //= 2
    f = 3
    while f ** 2 <= n:
        if n % f == 0:
            L.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        L.append(n)
    return L


a = 2 ** 62 - 1
b = 2 ** 102 - 1
print(a)
print(b)
c = trial_division(a)
d = trial_division(b)
print(c)
print(d)
