def is_tidy(N):
    N = str(N)
    last = '0'
    for i in N:
        if last < i:
            last = i
        elif last == i:
            continue
        else:
            return False
    return True


f = open('B-large-practice.in')
f.readline()
casenum = 1
for line in f:
    print('Case #{}: '.format(casenum), end='')
    casenum += 1
    N = int(line.rstrip())
    power = 1
    while(not is_tidy(N)):
        minus = (N % pow(10, power)) // pow(10, power - 1) + 1
        if minus != 10:
            N -= minus * pow(10, power - 1)
            power = 1
        else:
            power += 1
    print(N)
