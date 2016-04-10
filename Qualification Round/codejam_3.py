#!/usr/bin/env python3
import math

T = int(input())

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

"""def is_prime2(n, exclude=[]):
    fallback = 0
    for i in range(3, n):
        if n % i == 0:
            fallback = i
            if i not in exclude:
                return i
    return fallback
"""

def is_prime2(n):
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
        if i > 1000:
            return 0
    return 0


def int2base(x, base):
    x = int(x)
    if x == 0:
        return base[0]
    digits = []
    while x > 0:
        digits.append(base[int(x % len(base))])
        x //= len(base)
    digits.reverse()
    return ''.join(digits)


def base2int(x, base):
    nb = 0
    str_x = str(x)
    for c in str_x:
        nb = nb * len(base) + base.index(c)
    return nb

bases = [
    "01",
    "012",
    "0123",
    "01234",
    "012345",
    "0123456",
    "01234567",
    "012345678",
    "0123456789",
]

def calc(nb_of_jamcode, size):
    res = []
    for jam in range((size - 2) ** 2):
        jam <<= 1
        jam += 2 ** (size - 1) + 1
        o = []
        str_jam = int2base(jam, "01")
        flag = True
        o.append("{0:>{width}}".format(str_jam, width=size))
        for base in bases:
            nb = base2int(str_jam, base)
            #print("nb: %s" % nb)
            ntd = is_prime2(nb)
            if ntd == 0:
                flag = False
                break
            o.append(ntd)
        #print(str(o))

        if flag:
            res.append(o)
            print("%s" % o[0], end="")
            for elem in o[1:]:
                print(" %s" % elem, end="")
            print("")
        if len(res) == nb_of_jamcode:
            break
    return res

for loop in range(T):
    N, J = map(int, input().split())
    #value = input()

    print("Case #%s:" % (loop + 1))
    calc(J, N)
    #for l in calc(J, N): # ou J
    #    print("%s" % l[0], end="")
    #    for elem in l[1:]:
    #        print(" %s" % elem, end="")
    #    print("")