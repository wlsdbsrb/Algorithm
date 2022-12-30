X = int(input()) #총가격

N = int(input()) #물건종류수
sum=0
for i in range(N):
    a,b=map(int,input().split())
    sum+=a*b
if(X==sum):
    print("Yes")
else:
    print("No")
