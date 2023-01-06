N = int(input())
cnt = 0
for i in range(1,N+1):
    if i < 100:
        cnt+=1
    elif i>=100:
        a=i//100
        b=i%100//10
        c=i%100%10
        if((b-a)==(c-b) or (a-b)==(b-c)):
            cnt+=1
print(cnt)