import random


def poly_hash(s, p, x):
    y = 1
    h = 0
    for i in range(0, len(s)):
        h += ord(s[i])*y
        if i != len(s)-1:
            y = (y % p) * x
    return h % p


def check_match(s, k, p, x, t_h):
    hashes = [0]*len(s)
    s_h = poly_hash(s, p, x)
    y = 1
    for i in range(n):
        y = (y*x) % p
    hashes[0] = s_h

    if s_h == t_h:
        return 0

    for i in range(1, len(s)):
        s_h = (x*hashes[i-1] + ord(s[-i]) - y*ord(s[-i])) % p
        hashes[i] = s_h
        if s_h == t_h:
            return i

    return -1


n = int(input())
s = input()
t = input()

p = 10**9+7
x = random.randint(2, p)
h = poly_hash(t, p, x)

print(check_match(s, n, p, x, h))
