#!/usr/bin/env python3

T = int(input())

inf_max = 0
lines_max = []


def fractal(pattern, comp):
    #s = list(pattern)
    s = pattern
    #pattern = list(pattern)
    for loop in range(comp - 1):
        tmp = ""
        for i in range(len(s)):
            tmp += "G" * len(pattern) if s[i] == "G" else pattern
        s = tmp
    return s

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

def permutation(len):
    arr = []
    for i in range(2 ** len):
        arr.append("{0:G>{width}}".format(int2base(i, "GL"), width=len))
    return arr

def count(permutations):
    arr = [0] * len(permutations[0])
    for loop in range(len(permutations[0])):
        for p in permutations:
            if "G" in p[loop]:
                arr[loop] += 1
    return arr

def fmax(c):
    m = 0
    pos = -1
    for loop in len(c):
        co = c[loop]
        if co > m:
            m = co
            pos = loop
    return m, pos


def combine(permutations, lines):
    nb = 0
    global inf_max
    global lines_max
    for p in permutations:
        for l in lines:
            if p[l] == "G":
                nb += 1
                break
    lines_max = lines if inf_max < nb else lines_max
    inf_max = nb if inf_max < nb else inf_max
    #print(lines)
    return nb


def find(permutations, co, studs):
    for pos in range(len(co)):
        res = find_r(permutations, [pos], co, studs - 1)
        if res:
            return res

def find_r(permutations, lines, co, studs):
    if combine(permutations, lines) == len(permutations) - 1:
        return lines
    if studs == 0:
        return False
    for pos in range(len(co)):
        d = list(lines)
        d.append(pos)
        #print(">> %s" % pos)
        res = find_r(permutations, d, co, studs - 1)
        if res:
            return res
    return False

def calc(len_seq, complexity, students):
    #print("[%s]" % value)
    loop = 0
    permutations = []
    for perm in permutation(len_seq):
        permutations.append(fractal(perm, complexity))
    c = count(permutations)
    #for perm in permutations:
    #    print("".join(perm))
    #print(c)
    ma = max(c)
    mi = min(c)
    if ma == len(permutations) - 1:
        return "%s" % (c.index(ma) + 1)
    if ma != mi:
        # UNION?
        res = find(permutations, c, students)
        if res:
            res = list(set(res))
            return " ".join([str(x + 1) for x in res])
    if ma == mi and students == len(permutations[0]):
        return " ".join([str(x + 1) for x in range(students)])
    #print(permutation(3))
    #print("combinaison max : %s / %s" % (inf_max, len(permutations)))
    #print(" => %s" % (str(list(set(lines_max)))))
    return "IMPOSSIBLE"

for loop in range(T):
    inf_max = 0
    lines_max = []
    K, C, S = map(int, input().split())
    result = calc(K, C, S)
    print("Case #%s: %s" % (loop + 1, result))