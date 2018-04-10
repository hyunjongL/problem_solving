f = open('A-large-practice.in')
f.readline()
casenum = 1
for line in f:
    print('Case #{}: '.format(casenum), end='')
    casenum += 1
    pancakes, K = line.rstrip().split()
    K = int(K)
    pancakes = list((i == '+') for i in pancakes)
    flip = 0
    for i in range(len(pancakes) - K + 1):
        if not pancakes[i]:
            flip += 1
            for j in range(K):
                pancakes[i + j] = not pancakes[i + j]

    if False in pancakes[-K:]:
        print('IMPOSSIBLE')
    else:
        print(flip)
