#!/usr/bin/env python3


T = int(input())


def reverse(str, pos):
    if pos == 0:
        return str
    top = str[0:pos]
    bottom = str[pos:]
    str = ""
    for i in range(len(top)):
        str += "+" if top[i] == "-" else "-"
    top = str[::-1]
    return top + bottom

#Soit on bascule tout à - (surtout si il y a des moins après un +
# soit on prend le top de la stack pour compute le plus de +
# on peut aussi tout reverse

##
## Nouvelle approche : l'objectif est de "valider" le bas de la stack
# en plus asap, puis remonter
# on peut flip toute la stack si nécessaire
def count_plus(str):
    i = 0
    for c in str:
        if c == "+":
            i += 1
    return i
# simple greedy algorithm
def sub_calc_plus(val):
    max_plus = 0
    max_i = 0
    for i in range(len(val) + 1):
        s = count_plus(reverse(val, i))
        if s > max_plus:
            max_plus = s
            max_i = i
    return reverse(val, max_i)

def sub_calc_plus2(val, lastp):
    max_plus = 0
    max_i = 0
    for i in range(lastp + 1): # ou just lastp
        s = count_plus(reverse(val, i))
        if s > max_plus:
            max_plus = s
            max_i = i
    return reverse(val, max_i)

def sub_calc(val):
    try:
        lastp = val.index("+")
    except:
        lastp = -1
    try:
        lastm = val.index("-")
    except:
        lastm = 0
    #print("lastp: %s, lastm: %s" %(lastp, lastm))
    pivot = max(lastm, lastp)
    #if lastm > lastp:
    #    print("lastm > lastp: %s -> %s" % (val, reverse(val, 0)))
    #    #return reverse(val, lastp + 1)
    #    return reverse(val, len(val))
    #return sub_calc_plus2(val, pivot)
    if lastp == -1:
       return reverse(val, len(val))
    return reverse(val, pivot)

def calc(value):
    #print("[%s]" % value)
    loop = 0
    while loop < 10000:
        cc = 0
        for c in value:
            if c == "+":
                cc += 1
        if cc == len(value):
            return loop
        value = sub_calc(value)
        #print("%s: %s" % (loop, value))
        loop += 1

    return "IMPOSSIBLE"

for loop in range(T):
    value = input()
    result = calc(value)
    print("Case #%s: %s" % (loop + 1, result))