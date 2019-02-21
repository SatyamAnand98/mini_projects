# works only in Jupyter notebook
'''
from IPython.display import clear_output
clear_output()
'''
# in other IDE's we can use "print('\n'*100)"

board_position = ['1','2','3','4','5','6','7','8','9']
player2 = player1 =  ''
flag = c = 0

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def player_input():
    marker = ''
    while not(marker=='X' or marker=='O'):
        marker = input("Player1: choose X or O: ").upper()
        if marker =='X':
            return('X','O')
        else:
            return('O','X')

def display_board():
    for i in range(0,9,3):
        print(color.BOLD+color.GREEN+str(board_position[i])+color.END, end = "")
        print('|', end = "")
        print(color.BOLD+color.GREEN+str(board_position[i+1])+color.END, end = "")
        print('|', end = "")
        print(color.BOLD+color.GREEN+str(board_position[i+2])+color.END)
        if(i<6):
            print('--------')


def player1_move():
    move = int(input("Player 1 : Enter the position number: "))
    board_position[move-1] = player1
    for i in range(0,9,3):
        print(color.BOLD+color.GREEN+str(board_position[i])+color.END, end = "")
        print('|', end = "")
        print(color.BOLD+color.GREEN+str(board_position[i+1])+color.END, end = "")
        print('|', end = "")
        print(color.BOLD+color.GREEN+str(board_position[i+2])+color.END)
        if(i<6):
            print('--------')

def player2_move():
    move = int(input("Player 2 : Enter the position number: "))
    board_position[move-1] = player2
    for i in range(0,9,3):
        print(color.BOLD+color.GREEN+str(board_position[i])+color.END, end = "")
        print('|', end = "")
        print(color.BOLD+color.GREEN+str(board_position[i+1])+color.END, end = "")
        print('|', end = "")
        print(color.BOLD+color.GREEN+str(board_position[i+2])+color.END)
        if(i<6):
            print('--------')

def win_check():
    return((board_position[0]==board_position[1] and board_position[1]==board_position[2])or
    (board_position[3]==board_position[4] and board_position[4]==board_position[5])or
    (board_position[6]==board_position[7] and board_position[7]==board_position[8])or
    (board_position[0]==board_position[4] and board_position[4]==board_position[8])or
    (board_position[2]==board_position[4] and board_position[4]==board_position[6])or
    (board_position[0]==board_position[3] and board_position[3]==board_position[6])or
    (board_position[1]==board_position[4] and board_position[4]==board_position[7])or
    (board_position[2]==board_position[5] and board_position[5]==board_position[8]))


display_board()
print("Player 1: Choose Your Symbol X or O")
player1, player2 = player_input()

while(c<10):
    if(flag!=1 and c<9):
        print('\n'*100)
        display_board()
        player1_move()
        if(win_check() == 1):
            print("Player1 WON!!")
            exit(0)
        c = c+1
    else:
        break

    if(flag!=1 and c<9):
        print('\n'*100)
        display_board()
        player2_move()
        if(win_check() == 1):
            print("Player2 WON!!")
            exit(0)
        c += 1
    else:
        break
