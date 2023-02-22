import random

fint = open('../ex8/input.txt', 'r')
fout = open('output.txt', 'w')
answers = []
answer = [0, 0, 0]
x = fint.read().strip().split('\n')


def poly_hash(s, p, x):
    y = 1
    h = 0
    for i in range(0, len(s)):
        h += ord(s[i])*y
        if i != len(s)-1:
            y = (y % p) * x
    return h % p


def precompute(s, k, p, x):
    h = {}
    string = s[-k:]
    hashes = [0]*(len(s)-k+1)
    key = poly_hash(string, p, x)
    y = 1
    for i in range(len(string)):
        y = (y*x) % p
    hashes[len(s)-k] = key
    h[key] = len(s)-k
    for i in range(len(s)-k-1, -1, -1):
        new_hash = (x*hashes[i+1] + ord(s[i]) - y*ord(s[i + k])) % p
        h[new_hash] = i
        hashes[i] = new_hash
    return h


def are_equal(s, t):
    if s == t:
        return True
    else:
        return False


def search_common_subs(s_hash, t_hash, t, s, k):
    common_subs = list(set(s_hash.keys() & set(t_hash.keys())))
    for i in common_subs:
        if are_equal(s[s_hash[i]:s_hash[i]+k], t[t_hash[i]:t_hash[i]+k]):
            return s_hash[i], t_hash[i]


def binary_search(s, t, first, last):
    if first > last:
        return -1
    global answer
    k = (first+last)//2
    p = 10**9+7
    x = random.randint(2, p-1)
    s_hash = precompute(s, k, p, x)
    t_hash = precompute(t, k, p, x)
    indexes = search_common_subs(s_hash, t_hash, t, s, k)
    if indexes:
        answer = [indexes[0], indexes[1], k]
        binary_search(s, t, k+1, last)
    else:
        binary_search(s, t, first, k-1)


for i in x:
    strings = i.split()
    binary_search(strings[0], strings[1], 1, min(len(strings[0]), len(strings[1])))
    answers.append(answer)
    answer = [0, 0, 0]

for i in answers:
    fout.write(' '.join([str(j) for j in i])+'\n')
