board = []
sum = 0
for i in range(8):
    board.append(input())

for i in range(8):
    for j in range(8):
        if((i+j)%2==0):
            if board[i][j] == 'F':
                sum = sum + 1
print(sum)