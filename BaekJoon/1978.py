N = int(input())

prime = list(map(int,input().split()))
cnt = 0
for i in prime[:]:
    div = 0
    for j in range(1,i+1):
        if(i%j==0):
            div+=1
    if (div == 2):
        cnt += 1
print(cnt)