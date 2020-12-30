# Importing necessary libraries

# Import sys library
import sys
# Import random library
import random

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
    print("\n")


# Function to check winning combinations of computer and Player also.
def Winning_combinations():
    # winning combinations of Computer using X
    # Computer win with horizontal Possible combinations
    if(dic[1] =="X" and dic[2] =="X" and dic[3] =="X"):
        print("You loss!!!\n")
        return True
    if(dic[4] =="X" and dic[5] =="X" and dic[6] =="X"):
        print("You loss!!!\n")
        return True
    if(dic[7] =="X" and dic[8] =="X" and dic[9] =="X"):
        print("You loss!!!\n")
        return True

    # Computer win with vertical Possible combinations
    if(dic[1] =="X" and dic[4] =="X" and dic[7] =="X"):
        print("You loss!!!\n")
        return True
    if(dic[2] =="X" and dic[5] =="X" and dic[8] =="X"):
        print("You loss!!!\n")
        return True
    if(dic[3] =="X" and dic[6] =="X" and dic[9] =="X"):
        print("You loss!!!\n")
        return True

    # Computer win with Digonal Possible combinations
    if(dic[1] =="X" and dic[5] =="X" and dic[9] =="X"):
        print("You loss!!!\n")
        return True
    if(dic[3] =="X" and dic[5] =="X" and dic[7] =="X"):
        print("You loss!!!\n")
        return True


    # winning combinations of Player using O
    # Player win with horizontal Possible combinations
    if(dic[1] =="O" and dic[2] =="O" and dic[3] =="O"):
        print("You Won!!!\n")
        return True
    if(dic[4] =="O" and dic[5] =="O" and dic[6] =="O"):
        print("You Won!!!\n")
        return True
    if(dic[7] =="O" and dic[8] =="O" and dic[9] =="O"):
        print("You Won!!!\n")
        return True

    # Player win with vertical Possible combinations
    if(dic[1] =="O" and dic[4] =="O" and dic[7] =="O"):
        print("You Won!!!\n")
        return True
    if(dic[2] =="O" and dic[5] =="O" and dic[8] =="O"):
        print("You Won!!!\n")
        return True
    if(dic[3] =="O" and dic[6] =="O" and dic[9] =="O"):
        print("You Won!!!\n")
        return True

    # Player win with Digonal Possible combinations
    if(dic[1] =="O" and dic[5] =="O" and dic[9] =="O"):
        print("You Won!!!\n")
        return True
    if(dic[3] =="O" and dic[5] =="O" and dic[7] =="O"):
        print("You Won!!!\n")
        return True
    
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
def Player_moves(M, lis):

    # To check the correct move, is it repeating or not
    for i in lis:
        if(i == M):
            lis.remove(i)
            dic[M]="O"
            Board_design()
            break
    else:
        print("Please Enter the currect move!!")
        Input_moves()


# Function to take input from Player and also with stoping conditions
def Input_moves():
    
    move_count = 0
    Temp = 0
    while(True):                                                        
        move = int(input("Make Your Move ! [1-9] : " ))
        Player_moves(move, lis)
        move_count +=1
        if(Winning_combinations()==True):
            Temp = 1
            break
        if(move_count==9):
            break
        else:
            Computers_moves(lis)
            move_count +=1
            if(Winning_combinations()==True):
                Temp = 1
                break
            if(move_count==9):
                break
    if(Temp == 0):
        print("$$$  Deuce!  $$$\n")  

# main Function where from program execution starts
if __name__ == "__main__":

    # Defining the positions with the help of dict.
    # These are the 9 possible moves.
    dic = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}
    
    # Required for checking doublicate moves
    lis = [1,2,3,4,5,6,7,8,9]

    print("\nYour Moves == 'O'  and  Computers moves == 'X' ")

    Board_design()
    Input_moves()