M = int(input())
N = int(input())
num = set(list(map(int,input().split())))
rev_num = list(num)[::-1]
cnt = 0

for i in rev_num:
    for j in num:
        if (i == j):
            continue
        elif (i+j == N):
            cnt = cnt + 1

print(int(cnt/2))