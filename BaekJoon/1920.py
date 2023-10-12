f_num = int(input())
f_list = set(list(map(int, input().split())))
s_num = int(input())
s_list = list(map(int, input().split()))


for j in range(s_num):
    if s_list[j] in f_list:
        print('1')
    else:
        print('0')
