def log_base_2(N):
    result = 0
    while(N >= 1):
        result += 1
        N = N // 2
    return result

f = open('C-small-practice-2.in')
f.readline()
casenum = 1
for line in f:
    print('Case #{}: '.format(casenum), end='')
    casenum += 1
    stalls, people = line.rstrip().split()
    stalls = int(stalls)
    people = int(people)

    power = log_base_2(people) - 1
    power2 = pow(2, power)
    # 몫
    mokc = int((stalls - power2 + 1) // power2)
    remainder = int((stalls - power2 + 1) % power2)
    index = people - power2 + 1
    if remainder >= index:
        mokc += 1
    mokc -= 1
    print(mokc - mokc // 2, mokc // 2)
