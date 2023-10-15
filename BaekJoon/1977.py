M = int(input())
N = int(input())

sum = 0
list = []

for i in range(1,N):
    for j in range(M,N+1):
        if j==i**2:
            sum = sum + j
            list.append(j)
if sum==0:
    print('-1')
else:
    print(sum)
    print(min(list))