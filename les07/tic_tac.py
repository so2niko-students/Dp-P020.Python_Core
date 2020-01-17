'''
Tic-Tac-Toe game
'''
tictac = [[0,0,0],[0,0,0],[0,0,0]]

def draw_check():
    i = 0
    for tic in tictac:
        if all(tic):
            i += 1
    return 1 if i == 3 else 0

def print_tictac():
    for tic in tictac:
        print (tic,'\n')

def win(gamer):
    for i in range (3):
        if ((tictac[i][0] == gamer and tictac[i][1] == gamer and tictac[i][2] == gamer)
            or (tictac[0][i] == gamer and tictac[1][i] == gamer and tictac[2][i] == gamer)):
            return 1
        elif ((tictac[0][0] == gamer and tictac[1][1] == gamer and tictac[2][2] == gamer)
            or (tictac[2][0] == gamer and tictac[1][1] == gamer and tictac[0][2] == gamer)):
            return 1
    return 0
        
        
print ('В Ваш ход укажите координату')
i = 1
while 1:
    if i % 2 == 0:
        print_tictac()
        print ('Ход игрока 2\n')

        while 1: #Coordinate input
            
            vert = (int(input('введите номер столбца:'))) - 1
            while vert not in range (3):
                vert = (int(input('введите правильный номер столбца:'))) - 1
                
            goriz = (int(input('введите номер строки:'))) - 1
            while goriz not in range (3):
                goriz = (int(input('введите правильный номер строки:'))) -1 

            if tictac[goriz][vert]:
                print('это поле уже занято, введите другое')
                continue
            else:
                tictac[goriz][vert] = 2
                break                      

        if win(2):
            print ("Игрок 2 победил!!!")
            print_tictac()
            break
        if draw_check():
            print ("Ничья...")
            print_tictac()
            break

    else:
        print_tictac()
        print ('Ход игрока 1\n')

        while 1: #Coordinate input
            
            vert = (int(input('введите номер столбца:'))) - 1
            while vert not in range (3):
                vert = (int(input('введите правильный номер столбца:'))) - 1
                
            goriz = (int(input('введите номер строки:'))) - 1
            while goriz not in range (3):
                goriz = (int(input('введите правильный номер строки:'))) -1 

            if tictac[goriz][vert]:
                print('это поле уже занято, введите другое')
                continue
            else:
                tictac[goriz][vert] = 1
                break                      

        if win(1):
            print ("Игрок 1 победил!!!")
            print_tictac()
            break
        if draw_check():
            print ("Ничья...")
            print_tictac()
            break
 
    i+=1
