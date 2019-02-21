# works only in Jupyter notebook
'''
from IPython.display import clear_output
clear_output()
'''
# in other IDE's we can use "print('\n'*100)"

board_position = ['1','2','3','4','5','6','7','8','9']
player2 = player1 =  ''

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

display_board()
flag = c = 0
player2 = ''
print("Player 1: Choose Your Symbol X or O")
player1 = input()

if(player1=='X'):
    player2 = 'O'
elif(player1=='O'):
    player2 = 'X'
else:
    print("wrong option entered")
    exit(0)


while(c<10):
    if(flag!=1 and c<9):
        print('\n'*100)
        display_board()
        player1_move()
        if(board_position[0]==board_position[1] and board_position[1]==board_position[2]):
            flag = 1
            if(board_position[0]==player1):
                print("Player 1 Won!!")
                break
            elif(board_position[0]==player2):
                print("Player 2 Won!!")
                break
        if(board_position[3]==board_position[4] and board_position[4]==board_position[5]):
            flag = 1
            if(board_position[3]==player1):
                print("Player 1 Won!!")
                break
            elif(board_position[3]==player2):
                print("Player 2 Won!!")
                break
        if(board_position[6]==board_position[7] and board_position[7]==board_position[8]):
            flag = 1
            if(board_position[6]==player1):
                print("Player 1 Won!!")
                break
            elif(board_position[6]==player2):
                print("Player 2 Won!!")
                break
        if(board_position[0]==board_position[4] and board_position[4]==board_position[8]):
            flag = 1
            if(board_position[0]==player1):
                print("Player 1 Won!!")
                break
            elif(board_position[0]==player2):
                print("Player 2 Won!!")
                break
        if(board_position[2]==board_position[4] and board_position[4]==board_position[6]):
            flag = 1
            if(board_position[2]==player1):
                print("Player 1 Won!!")
                break
            elif(board_position[2]==player2):
                print("Player 2 Won!!")
                break
        if(board_position[0]==board_position[3] and board_position[3]==board_position[6]):
            flag = 1
            if(board_position[0]==player1):
                print("Player 1 Won!!")
                break
            elif(board_position[0]==player2):
                print("Player 2 Won!!")
                break
        if(board_position[1]==board_position[4] and board_position[4]==board_position[7]):
            flag = 1
            if(board_position[1]==player1):
                print("Player 1 Won!!")
                break
            elif(board_position[1]==player2):
                print("Player 2 Won!!")
                break
        if(board_position[2]==board_position[5] and board_position[5]==board_position[8]):
            flag = 1
            if(board_position[2]==player1):
                print("Player 1 Won!!")
                break
            elif(board_position[2]==player2):
                print("Player 2 Won!!")
                break
        c = c+1
    else:
        break

    if(flag!=1 and c<9):
        print('\n'*100)
        display_board()
        player2_move()
        if(board_position[0]==board_position[1] and board_position[1]==board_position[2]):
            flag = 1
            if(board_position[0]==player2):
                print("Player 2 Won!!")
                break
            elif(board_position[0]==player1):
                print("Player 1 Won!!")
                break
        if(board_position[3]==board_position[4] and board_position[4]==board_position[5]):
            flag = 1
            if(board_position[3]==player2):
                print("Player 2 Won!!")
                break
            elif(board_position[3]==player1):
                print("Player 1 Won!!")
                break
        if(board_position[6]==board_position[7] and board_position[7]==board_position[8]):
            flag = 1
            if(board_position[6]==player2):
                print("Player 2 Won!!")
                break
            elif(board_position[6]==player1):
                print("Player 1 Won!!")
                break
        if(board_position[0]==board_position[4] and board_position[4]==board_position[8]):
            flag = 1
            if(board_position[0]==player2):
                print("Player 2 Won!!")
                break
            elif(board_position[0]==player1):
                print("Player 1 Won!!")
                break
        if(board_position[2]==board_position[4] and board_position[4]==board_position[6]):
            flag = 1
            if(board_position[2]==player2):
                print("Player 2 Won!!")
                break
            elif(board_position[2]==player1):
                print("Player 1 Won!!")
                break
        if(board_position[0]==board_position[3] and board_position[3]==board_position[6]):
            flag = 1
            if(board_position[0]==player2):
                print("Player 2 Won!!")
                break
            elif(board_position[0]==player1):
                print("Player 1 Won!!")
                break
        if(board_position[1]==board_position[4] and board_position[4]==board_position[7]):
            flag = 1
            if(board_position[1]==player2):
                print("Player 2 Won!!")
                break
            elif(board_position[1]==player1):
                print("Player 1 Won!!")
                break
        if(board_position[2]==board_position[5] and board_position[5]==board_position[8]):
            flag = 1
            if(board_position[2]==player2):
                print("Player 2 Won!!")
                break
            elif(board_position[2]==player1):
                print("Player 1 Won!!")
                break
        c += 1
    else:
        break
