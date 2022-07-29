import numpy as np
from itertools import combinations


def get_divisors(n):
    divisors = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divisors.append(i)
    divisors.append(n)
    return divisors[0:len(divisors) - 1]


def find_amicable_numbers(num1, num2, logs=False):
    a = num1
    b = num2

    diva = get_divisors(a)
    divb = get_divisors(b)

    if np.sum(diva) == num2 and num1 == np.sum(divb):
        print('Numbers ' + str(num1) + ' ' + str(num2) + ' are amicable')
        return 1
    if logs:
        print('Numbers ' + str(num1) + ' ' + str(num2) + ' are not amicable')
    return 0


find_amicable_numbers(220, 284, logs=True)

numbers = list(range(221, 2000))
pairs = list(combinations(numbers, 2))
for i in pairs:
    if find_amicable_numbers(i[0], i[1], logs=False) != 0:
        print('Next pair of amicable numbers is : (' + str(i[0]) + ', ' + str(i[1]) + ')')
        break
