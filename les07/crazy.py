# TIC TAC TOE
import random

def genGame():
    rand = 0

    tic_tac = []
    for row in range(0, 3):
        row = []
        tic_tac.append(row)
        
        for elem in range(0, 3):
            rand = random.randint(0,2)
            row.append(rand)

    return tic_tac

def showGame(tic_tac):
    print(f"-------------")
    print(f"|--{tic_tac[0][0]}--{tic_tac[0][1]}--{tic_tac[0][2]}--|")
    print(f"-----------")
    print(f"|--{tic_tac[1][0]}--{tic_tac[1][1]}--{tic_tac[1][2]}--|")
    print(f"-----------")
    print(f"|--{tic_tac[2][0]}--{tic_tac[2][1]}--{tic_tac[2][2]}--|")
    print(f"-------------")

def count_tic_tac(tic_tac):      
    count_o = 0
    count_x = 0 
    count_zero = 0
    for raw in tic_tac:
        for elem in raw:
            if elem == 0:
                count_zero += 1
            if elem == 1:
                count_x += 1
            if elem == 2:
                count_o += 1

    
    if checkWinner(tic_tac, 1):
        print("Победил Х")
        return
    elif checkWinner(tic_tac, 2):
        print("Победил O")
        return
            
    if count_zero == 0:
        print("Ничья!")
        return
    else:
        print("Победителя нет, игра продолжается!")


def checkWinner(tic_tac, gamer):
    if tic_tac[0][0] == tic_tac[0][1] == tic_tac[0][2] == gamer or\
       tic_tac[0][0] == tic_tac[1][0] == tic_tac[2][0] == gamer or\
       tic_tac[1][0] == tic_tac[1][1] == tic_tac[1][2] == gamer or\
       tic_tac[2][0] == tic_tac[2][1] == tic_tac[2][2] == gamer or\
       tic_tac[0][0] == tic_tac[1][1] == tic_tac[2][2] == gamer or\
       tic_tac[0][1] == tic_tac[1][1] == tic_tac[2][1] == gamer or\
       tic_tac[0][2] == tic_tac[1][2] == tic_tac[2][2] == gamer or\
       tic_tac[0][2] == tic_tac[1][1] == tic_tac[2][0] == gamer:
        return True

    return False

            
game = genGame()
showGame(game)
count_tic_tac(game)
