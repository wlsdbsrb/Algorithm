N,K = map(int,input().split())
a=[]
cnt=0
for i in range(N):
    x = int(input())
    a.append(x)
    a.sort(reverse=True)
for i in a:
    cnt+=K//i
    K= K%i
print(cnt)