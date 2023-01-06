N = int(input())
for i in range(N):
    VPS = input()
    sum=0
    for j in range(len(VPS)):
        if(VPS[j]=='('):
            sum+=1
        elif(VPS[j]==')'):
            sum-=1
        if (sum<0):
            print('NO')
            break
    if(sum==0):
        print('YES')
    elif(sum>0):
        print('NO')