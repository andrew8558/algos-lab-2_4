fint = open('input.txt')
fout = open('output.txt', 'w')
x = fint.readline().strip().split()
s = ''.join(x)

letters = {}
for i in range(len(s)):
    if s[i] in letters.keys():
        letters[s[i]].append(i)
    else:
        letters[s[i]] = [i]

count = 0
for i in letters.values():
    if len(i) != 1:
        x = i[-1] - i[0] - 1
        variants = len(i) * (len(i) - 1) // 2
        count += x * variants
        for j in range(1, len(i) - 1):
            count -= (i[-1] - i[j]) * j + (i[j] - i[0]) * (len(i) - j - 1)

fout.write(str(count))
