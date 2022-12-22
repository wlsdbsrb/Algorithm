1026
S = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
sum = 0
x.sort(reverse=False)
y.sort(reverse=True)
for i in range(S):
    sum += x[i]*y[i]
print(sum)


