M = int(input())
N = int(input())
sosu_list=[]
for i in range(M,N+1):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt == 2:
        sosu_list.append(i)
if len(sosu_list) > 0 :
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)