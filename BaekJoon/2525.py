hour, minute = map(int,input().split())
time=int(input())
hour1 = (minute + time) // 60
minute1 = (minute + time) % 60

if(minute+time>=60):
    if(hour+hour1>=24):
        print(hour + hour1 - 24, minute1)
    else:
        print(hour + hour1, minute1)
else:
    print(hour,minute+time)