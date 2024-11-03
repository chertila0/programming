# #1
import itertools
alp = "ТИМОФЕЙ"
ar = itertools.product(alp, repeat=5) 
arl = []
for i in ar:
    arl.append(''.join(i))

count = 0
for e in arl:
    e[0] == 'Й'
    e[-1] == 'Й'
    if e.count('Й') > 1:
        continue
    if  e.startswith('Й'):
        continue
    if  e.endswith('Й'):
        continue
    flag = True
    for i in range(len(e)-1):
        if (e[i] == 'Й' and e[i + 1] == 'И') or (e[i + 1] == 'Й' and e[i] == 'И'):
           flag = False
           break
    if flag == True: count += 1
print(count)

#2
n = 4**2020 + 2**2017 - 15
s = bin(n)[2:]
print(s.count('1'))

#3
a = 174457
b = 174505
k = 0
for n in range(a, b + 1):
    ds = []
    for d in range(2, n//2 + 1):
        if n % d == 0:
            ds.append(d)
            if len(ds) > 2:
                break
    if len(ds) == 2:
        print(ds[0], ds[1], ds[0]*ds[1])