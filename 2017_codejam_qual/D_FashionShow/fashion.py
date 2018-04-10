

f = open('D-large-practice.in')
f.readline()
casenum = 1
for line in f:
    print('Case #{}: '.format(casenum), end='')
    casenum += 1
    X = line.rstrip()
