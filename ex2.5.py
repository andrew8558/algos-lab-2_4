import random

fint = open('input.txt', 'r')
fout = open('output.txt', 'w')
indexes = []


def poly_hash(s, p, x):
    y = 1
    h = 0
    for i in range(0, len(s)):
        h += ord(s[i])*y
        if i != len(s)-1:
            y = (y % p) * x
    return h % p


def check_match(s, k, p, x, t_h):
    string = s[-k:]
    hashes = [0]*(len(s)-k+1)
    s_h = poly_hash(string, p, x)
    y = 1
    for i in range(len(string)):
        y = (y*x) % p
    hashes[len(s)-k] = s_h

    if s_h == t_h:
        indexes.append(len(s)-k)

    for i in range(len(s)-k-1, -1, -1):
        s_h = (x*hashes[i+1] + ord(s[i]) - y*ord(s[i + k])) % p
        hashes[i] = s_h
        if s_h == t_h:
            indexes.append(i)


s = fint.readline().strip()
t = fint.readline().strip()

p = 10**9+7
x = random.randint(2, p)
h = poly_hash(t, p, x)
check_match(s, len(t), p, x, h)

indexes.reverse()
fout.write(' '.join([str(i) for i in indexes]))
