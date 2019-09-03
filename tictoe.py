#Milestone Project 1 - UdemyCourse - Jogo da Velha

import random

board = ['1','2','3','4','5','6','7','8','9']
def display_board(board):        
    print(f'\n{board[6]} | {board[7]} | {board[8]}')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(f'{board[0]} | {board[1]} | {board[2]}\n')

def player_input():
    a = ''
    while (a!= 'X' or a!='O'):
        a = input('Please, starts with "X" or "O": ')
        if a == 'X' or a == 'O':
            return a.upper()
        else:
            print('Please, type "X" or "O" capitalized.')
            

def place_marker(board,marker,position):
    board[position-1] = marker

def win_check(board, mark):
    if board[0] == board[1] ==  board[2] == mark:
        return True
    elif board[3] == board[4] ==  board[5] == mark:
        return True
    elif board[6] == board[7] ==  board[8] == mark:
        return True
    ##
    elif board[0] == board[3] ==  board[6] == mark:
        return True
    elif board[1] == board[4] ==  board[7] == mark:
        return True
    elif board[2] == board[5] ==  board[8] == mark:
        return True
    ##
    elif board[6] == board[4] ==  board[2] == mark:
        return True
    elif board[0] == board[4] ==  board[8] == mark:
        return True

    else:
        pass
        
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position-1] != ('X' or 'O')

def full_board_check(board):
    for i in board:
        if i == 'X' or i == 'O':
            pass
        else:
            return False
    return True

def player_choice(board):
    while True:
        try:
            z = int(input("Type the number according to the map that you want mark: "))
            if z>0 and z<10:
                break
            else:
                print('You must type a integer number between 1 and 9')
                continue

        except ValueError:
            print('You must type a integer NUMBER between 1 and 9')
    
    if space_check(board,z):
        return z
    else:
        return False

def replay():
    c = input('Do you want to play again: [y][n]?')
    return c.lower() =='y'

def second_input(o):
    if o == 'X':
        print(f'"O" is your turn')
        return 'O'
        
    else:
        print(f'"X" is your turn')
        return 'X'



## The main function starts here:
print('\n'*100)
n1 = input('Type the name of the first player: ')
n2 = input('Type the name of the second player: ')
print('\n'*100)
print(f'Welcome {n1} and {n2} to Tic Tac Toe Game!')
print('We are gonna play now! Please pay attention to the instructions below.')
print('This is the board that we will utilize, and you should select the number according to the map:')
display_board(board)
print("Now, let's play\n\n\n") 

o = player_input()
while not full_board_check(board):
    z = player_choice(board)
    if z != False:
        place_marker(board,o,z)
        if win_check(board,o) == True:
            print('\n'*100)
            print(f'****** {o} Wins the Game!******')
            display_board(board)
            if not replay():
                break
            else:
                board = ['1','2','3','4','5','6','7','8','9']
                display_board(board)
                continue
        display_board(board)
        o = second_input(o)    
    else:
        print(f'This space is full. Try another one')
        continue
else:
    print("\n\n YOU DRAWN THE GAME!!")
