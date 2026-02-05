
def canPlaceQueen(b,r,c):
    
    print("Checking that can we place queen on ",b)
    for i in range(r):
        if b[i][c] == 1:
            return False
        
    for i in range(c):
        if b[r][i] == 1:
            return False
    
    i=r-1
    j=c-1
    while i>=0 and j>=0:
        if b[i][j]==1:
            return False
        i-=1
        j-=1

    i=r-1
    j=c+1
    while i>=0 and j<n:
        if b[i][j]==1:
            return False
        j+=1
        i-=1
        
    return True


def n_queens(board,row,col):

    if row==n:
        print("*************************************************NOT Possible***********************************************")
        print()
        return
    if col == n:
        print("*************************************************NOT Possible***********************************************")
        print()
        return 

    print(row, col)

    if canPlaceQueen(board,row,col):
        board[row][col] = 1
        if row == n-1:
            print("############### N Queens Possible board########## ",board)
            return 
        else:
            print("Placed --> Board with queen placed: ",board)
            n_queens(board,row+1,0)
    else:
        print("Not placed")
        n_queens(board,row,col+1)
    
    return 

board = []
n=4

for row in range(n):
    row = []
    for col in range(n):
        row.append(0)
    board.append(row)

for col in range(n):
    b = [r[:] for r in board]
    n_queens(b,0,col)