import itertools
import search
import sokoPuzzle
import node

board = search.board7
height = len(board)
width = len(board[0])
def isdeadlock(board) : 
        for i,j in itertools.product(range(height), range(width)) :
                if (board[i][j]== ' ' or board[i][j]=='R') :  
                    if board[i-1][j] and board[i][j-1] : 
                        board[i][j] = 'D'
                    elif board[i+1][j] == ' ' or board[i][j+1] :
                        board[i][j] = 'D'
        return board

isdeadlock(board)


        
