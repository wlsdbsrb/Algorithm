import sys
N = int(sys.stdin.readline())
dis = list(map(int,sys.stdin.readline().split()))
money = list(map(int,sys.stdin.readline().split()))
first = dis[0] * money[0]
min_money = money[0]
for i in range(1,N-1):
    if min_money > money[i]:
        min_money = money[i]
    first = first+ min_money * dis[i]
print(first)