T = int(input())
b=1
for i in range(T):
    k = int(input())
    n = int(input())
    k0 = [x for x in range(1,n+1)]
    for k in range(k):
        for i in range(1,n):
            k0[i] += k0[i-1]
    print(k0[-1])