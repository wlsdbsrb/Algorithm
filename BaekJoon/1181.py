import sys
N = int(sys.stdin.readline())
a=[]
for i in range(N):
    a.append(sys.stdin.readline().strip())
set_a=set(a)
a=list(set_a)
a.sort()
a.sort(key=len)
for i in a:
    print(i)