# list all odd primes no bigger than an input number N
# uses a formulae in function "prime()" defined here, which returns either number 2 or a prime
# input N should NOT be very big, say more than 25000, on a typical PC
# otherwise, time consumed will be unacceptable (hours)
# I think mostly the time run by the prog is consumed in function "factorial()"
# especially, it is repeated nearly N-square in this program
# I should improve the algorithm
# written by H D Duan, July 2021

from datetime import datetime
from math import factorial


def fact(n):
    res = 1
    for i in range(1, n + 1, 1): res *= i
    return res


def prime(m):
    # this will return an array of all prime numbers not bigger than the integer m
    pr = [0] * m
    cc = 0
    for k in range(2, m, 2):
        # primeno=int((factorial(k)%(k+1))/k)*(k-1)+2
        ff = factorial(k)
        primeno = int((ff % (k + 1)) / k) * (k - 1) + 2
        # print(k, ff, primeno, '\n')
        if primeno != 2:
            cc += 1
            pr[cc] = primeno

    pr = pr[1:cc + 1]  # trim the array pr to get only the nonzeros, which are primes
    return pr


#####
# Main
#####
import sys
import numpy

m = input('\nGive a positive integer: ')
if not m.isnumeric(): sys.exit('invalid input!')
m = int(m)
if m <= 0: sys.exit('must be positive int')
t0 = datetime.now()
print(t0)
pr_list = prime(m)
count = len(pr_list)
for n in range(1, 10, 1): pr_list.append(0)
if count > 9:
    for l in range(0, count, 9):
        print(pr_list[l:l + 9])
else:
    print(pr_list)
print('\n(Zeros are ignored from the list!)')
t1 = datetime.now()
print('\nTime elapsed (sec): ', str(t1 - t0))
print('\nThere are ', count, ' odd primes not greater than ', m)
print('\nActually these are all odd prime numbers not bigger than ', m)
print('\nThe ratio is ', count / m, '\n\n')
