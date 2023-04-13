n = int(input())
for i in range(n):
    x = []
    y = []
    L_list = []
    R_list = []
    word = list(map(str,input()))
    x_num = 0
    y_num = 0
    x.append(0)
    y.append(0)
    for j in word:
        if j == 'R':
            R_list.append(j)
        if j == 'L':
            L_list.append(j)
        if j == 'F':
            if (len(L_list)%4-len(R_list)%4) == 0:
                y_num+=1
                y.append(y_num)
            if (len(L_list)%4-len(R_list)%4) == 1 or (len(R_list)%4-len(L_list)%4 == 3):
                x_num-=1
                x.append(x_num)
            if (len(L_list)%4-len(R_list)%4) == 2 or (len(R_list)%4-len(L_list)%4 == 2):
                y_num-=1
                y.append(y_num)
            if (len(L_list)%4-len(R_list)%4) == 3 or (len(R_list)%4-len(L_list)%4 == 1):
                x_num+=1
                x.append(x_num)
        if j == 'B':
            if (len(L_list)%4-len(R_list)%4) == 0:
                y_num-=1
                y.append(y_num)
            if (len(L_list)%4-len(R_list)%4) == 1 or (len(R_list)%4-len(L_list)%4 == 3):
                x_num+=1
                x.append(x_num)
            if (len(L_list)%4-len(R_list)%4) == 2 or (len(R_list)%4-len(L_list)%4 == 2):
                y_num+=1
                y.append(y_num)
            if (len(L_list)%4-len(R_list)%4) == 3 or (len(R_list)%4-len(L_list)%4 == 1):
                x_num-=1
                x.append(x_num)
    result = ((max(x)-min(x)) * (max(y)-min(y)))
    print(result)