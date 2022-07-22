import math


def primitive_root(p):
    factorization = primeFactorization(p - 1)

    roots = []
    for a in range(2, p - 1):
        flag = True
        for i in range(len(factorization)):
            res = pow(int(a), int((p - 1) / factorization[i]), p)
            if res != 1:
                flag = True
            else:
                flag = False
                break
        if flag:
            roots.append(a)
    return sorted(set(roots))


def primeFactorization(num):
    result = []
    while num % 2 == 0:
        result.append(2)
        num = num / 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):

        while num % i == 0:
            result.append(i)
            num = num / i
    if num > 2:
        result.append(int(num))

    return result


for i in [5, 7, 11, 13, 17, 31]:
    print('Primitive roots of ' + str(i) + ' = ' + str(primitive_root(i)))
