king=1
queen=1
rook=2
bishop=2
knight=2
pawn=8
king2 , queen2, rook2, bishop2, knight2, pawn2 = map(int,input().split())
print((king-king2),(queen-queen2),(rook-rook2),(bishop-bishop2),(knight-knight2),(pawn-pawn2))