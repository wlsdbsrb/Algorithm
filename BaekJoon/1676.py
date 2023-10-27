N = int(input())
sum = 1
cnt = 0
for i in range(1,N+1):
    sum *= i
a = str(sum)
k = list(a)
list.reverse(k)
for i in k:
    if i=='0':
        cnt += 1
    elif i!='0':
        break
print(cnt)