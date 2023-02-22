fint = open('input.txt')
fout = open('output.txt', 'w')
x = fint.readline().strip().split()
s = ''.join(x)

z = [0]*len(s)
l = 0
r = 0
z[0] = 0

for i in range(1, len(s)):
    d = 0
    if i <= r:
        d = min(r-i+1, z[i-l])
    while i+d < len(s) and s[i+d] == s[d]:
        d += 1
    if i+d-1 > r:
        l = i
        r = i+d-1
    z[i] = d

x = [str(i) for i in z]
s = ' '.join(x[1:])
fout.write(s)
