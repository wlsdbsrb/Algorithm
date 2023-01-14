import sys
N = int(sys.stdin.readline())
list=[]
for i in range(N):
    a,b = map(str,sys.stdin.readline().split())
    list.append([int(a),i,b])
list.sort()
for i in range(N):
    print("%d %s"%(list[i][0],list[i][2]))