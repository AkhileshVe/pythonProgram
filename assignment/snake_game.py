#  ================================= Snakes and Ladders =================================
import random

pl1 = 0
pl2 = 0

snw_out= { 29:9, 38:15, 47:5, 53:33, 62:37, 86:54, 92:70, 97:25 }
law_out = { 2:23, 8:34, 20:77, 32:68, 41:79, 74:88, 85:95, 82:100 }

sn  = { 29:9, 38:15, 47:5, 53:33, 62:37, 86:54, 92:70, 97:25 }
la = { 2:23, 8:34, 20:77, 32:68, 41:79, 74:88, 85:95, 82:100 }

def first_player(player1,dice,snake,ladder):
    if(dice == 6):
            input("you get extra chance press 1 for through the dice for player1: ")
            print("you get the score is : ",dice)
            player1 += dice
        
    if player1 in snake:
        print("sanke is bitten you")
        player1 = snake[player1]

    if player1 in ladder:
        print("sidhi chado")
        player1 = ladder[player1]
    
    print("player1 is ",player1," place")

    
def second_player(player2,dice,snake,ladder,p2):
    if(dice == 6):
        input("you get extra chance press 2 for through the dice for player2: ")
        print("you get the score is : ",dice)
        player2 += dice        
    
    if player2 in snake:
        print("sanke is bitten you")
        player2 = snake[player2]
    
    if player2 in ladder:
        print("sidhi chado")
        player2 = ladder[player2]
    
    print("player2 is ",player2," place")

def Snakes_ladder(a,b,c,d):
    p1_data = []
    p2_data = []

    player1 = a
    player2 = b

    snake  = c
    ladder = d
     # first player
    while True:
        print()
        print("============= 1 ===================")
        print()
        input("press 1 for through the dice for player1: ")
        dice = random.randint(1,6)
        print("you get the score is : ",dice)
        p1_data.append(dice)
        player1 += dice
 
        first_player(player1,dice, snake,ladder)
        if player1 >=100 :
            print("player1 won the match")
            break
    
    # second player
        print()
        print("============= 2 ===================")
        print()
        input("press 2 for through the dice for player2 : ")
        dice = random.randint(1,6)
        print("you get the score is : ",dice)
    
        player2 += dice

        second_player(player2,dice, snake,ladder,p2_data)
            
        if player2 >=100 :
            print("player2 won the match")
            break

Snakes_ladder(pl1,pl2,sn,la)