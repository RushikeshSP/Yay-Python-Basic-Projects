# Importing necessary libraries

# Import sys library
import sys
# Import random library
import random

# Defining the positions with the help of dict.
# These are the 9 possible moves.
dic = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}

# Winning combinations
win_combi = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    
# Required for checking doublicate moves
lis = [i for i in range(1,10)]


# Function For Printing Board design in output
def Board_design():

    # The pattern of game board
    print("\n")
    print(dic[1]+" | "+dic[2]+" | "+dic[3])
    print("--+---+--")
    print(dic[4]+" | "+dic[5]+" | "+dic[6])
    print("--+---+--")
    print(dic[7]+" | "+dic[8]+" | "+dic[9])
    # print("----------------")
    # print("\n")


# Function to check winning combinations of computer and Player also.
def Winning_combinations():

    for i in win_combi:
        if(dic[i[0]] == dic[i[1]] == dic[i[2]] == "O"):
            print("##### Congratulations You Won The Game #####\n")
            return True
            # break
        if(dic[i[0]] == dic[i[1]] == dic[i[2]] == "X"):
            print("##### You Lost The Game #####\n")
            return True
            # break
    return False


# Function for Computer moves  
def Computers_moves(lis):
    # lis = [1,2,3,4,5,6,7,8,9]
    num = random.randint(1,9)  # This function to generate random numbers

    # To check the correct move, is it repeating or not
    for i in lis:
        if(i == num):
            lis.remove(i)
            dic[num]="X"
            print("Move made by Computer!! ")
            Board_design()
            break
    else:
        Computers_moves(lis)


# Function for Player moves  
def Player_moves(lis):

    try:
        move = int(input("Make Your Move ! [1-9] : " ))
    except Exception:
        print("Please Enter integer input as a move.")
        Player_moves(lis)
    else:
        # To check the correct move, is it repeating or not
        for i in lis:
            if(i == move):
                lis.remove(i)
                dic[move]="O"
                Board_design()
                break
        else:
            print("Please Enter the currect move!!")
            Player_moves(lis)


# Function to take input from Player and also with stoping conditions
def Input_moves():
    
    move_count = 0
    Temp = 0
    while(True):                                                        
        Player_moves(lis)
        move_count +=1
        if(Winning_combinations()):
            Temp = 1
            break
        if(move_count==9):
            break
        else:
            Computers_moves(lis)
            move_count +=1
            if(Winning_combinations()):
                Temp = 1
                break
            if(move_count==9):
                break
    if(Temp == 0):
        print("$$$  Deuce!  $$$\n")  


# main Function where from program execution starts
if __name__ == "__main__":

    print("\nYour Moves == 'O'  and  Computers moves == 'X' ")

    Board_design()
    Input_moves()