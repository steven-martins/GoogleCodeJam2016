#!/usr/bin/env python3


N = int(input())

def calc(value):
    m = {}
    for l in range(10):
        m["%s" % l] = 0
    for j in range(100):
        j += 1
        nb = j * value
        str = "%s" % nb
        for c in str:
            m[c] = 1

        counter = 0
        for k, v in m.items():
            if v == 1:
                counter += 1
        if counter == 10:
            return nb
    return "INSOMNIA"

for loop in range(N):
    value = int(input())
    result = calc(value)
    print("Case #%s: %s" % (loop + 1, result))