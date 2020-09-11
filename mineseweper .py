
import random
import time
import sys
sys.setrecursionlimit(100000)

def create_board(board_size, num_mines):
    
    global myboard
    global location_of_mines
    
    t=0
    while t<num_mines:
        row=random.randint(0,board_size-1)
        col=random.randint(0,board_size-1)
        if myboard[row][col] ==0: #if there already isn't a mine in this tile, we put a mine in it.
            myboard[row][col] = 1
            location_of_mines.append([row,col])
            t+=1

    return myboard


def print_board():
    global board_size
    global board
    for i in range(board_size):
        for j in range(board_size):
            print(board[i][j], end= "\t")
        print()
    
    return


def put_flag(row,col):
    
    global board
    board[row][col] = "p"
    return
    

def remove_flag(row, col):
    
    global board
    board[row][col]= "#"
    return


def count_mines(row,col):
        
    global myboard
    global board_size
    total=0
    #obviously row and col >=0 ; row and col < board_size
    if row-1>=0:
        if col-1 >= 0:
            if myboard[row-1][col-1]==1:
                total+=1
                
    if row-1 >=0:
        if myboard[row-1][col]==1:
            total+=1
            
    if row-1>=0:
        if col+1<board_size:
            if myboard[row-1][col+1]==1:
                total+=1
                
    if col-1>=0:
        if myboard[row][col-1]==1:
            total+=1
            
    if col+1<board_size:
        if myboard[row][col+1]==1:
            total+=1
    if col-1>=0:
        if row+1<board_size:
            if myboard[row+1][col-1]==1:
                total+=1
        
    if row+1<board_size:
        if myboard[row+1][col]==1:
            total+=1
            
    if row+1<board_size:
        if col+1 < board_size:
            if myboard[row+1][col+1]==1:
                total+=1
        
    board[row][col] = total
       
    return

    

def reveal_cell(row,col):
    if myboard[row][col] ==1:
        print("sorry you lost")
        return -1
    elif myboard[row][col] ==0:
        return count_mines(row, col)

    
def won():
    
    for i in range(board_size):
        for j in range(board_size):
            
            #if there's a tile neither flagged nor revealed,  the game continues:
            if board[i][j] == "#":
                return True
            
            #if there's a normal tile on which the player has put a flag by mistake, the game continues:
            elif myboard[i][j]== 0:
                if board[i][j] =="p" :
                    return True
            
            #if there's a mine on which the player hasn't put a flag , the game continues:
            elif myboard[i][j]==1:
                if board[i][j] != "p":
                    return True
                
            
            
            else:
                return False


def  main():
    global board_size
    global num_mines
    
    create_board(board_size, num_mines)
    
    check_won= won()
    
    while check_won==True :
        
        command= input("enter the command you like to run.(just enter r,f,u, or x):")
    
        if command== "r":
            row= int(input("enter the number of the row you wish to reveal.(the number must be between 0 and board_size -1):"))
            col=int(input("enter the number of the column you wish to reveal.(the number must be between 0 and boad_size-1):"))
            reveal_cell(row, col)
            
            a=reveal_cell(row, col)
            if a == -1:
                return
            print_board()
        
            
        if command =="u":
            row= int(input("enter the number of the row you wish to remove flag from, (the number must be between 0 and board_size -1):"))
            col=int(input("enter the number of the column you wish to remove flag from. (the number must be between 0 and board_size -1):"))
            remove_flag(row, col)
            print_board()
    
        if command == "f":
            row= int(input("enter the number of the row you wish to put flag on. (the number must be between 0 and board_size -1):"))
            col=int(input("enter the number of the column you wish to put flag on. (the number must be between 0 and board_size -1):"))
            put_flag(row, col)
            print_board()
        
        if command == "x":
            return
        
        check_won= won()
        
    print("congrats! you won.")
    return

board_size= int(input("please enter the size of the board:"))
num_mines=int(input("please enter the number of mines:"))
myboard= [[0 for i in range(board_size)]for j in range(board_size)]
board= [["#" for i in range(board_size)] for j in range(board_size)]
location_of_mines=[]

t0= time.time()
main()
t1=time.time()
time_consumed= t1 - t0
print("time consumed:",time_consumed, "seconds")