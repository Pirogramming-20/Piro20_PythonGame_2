from Player.Player import Player
import random

def gameStart():
    print('-'*80)
    print('''  /$$$$$$   /$$$$$$   /$$$$$$                                                   
    /$$__  $$ /$$__  $$ /$$__  $$                                                  
    |__/  \ $$| $$  \__/| $$  \ $$        /$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
    /$$$$$/| $$$$$$$ |  $$$$$$$       /$$__  $$ |____  $$| $$_  $$_  $$ /$$__  $$
    |___  $$| $$__  $$ \____  $$      | $$  \ $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$
    /$$  \ $$| $$  \ $$ /$$  \ $$      | $$  | $$ /$$__  $$| $$ | $$ | $$| $$_____/
    |  $$$$$$/|  $$$$$$/|  $$$$$$/      |  $$$$$$$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$
    \______/  \______/  \______/        \____  $$ \_______/|__/ |__/ |__/ \_______/
                                        /$$  \ $$                                  
                                        |  $$$$$$/                                  
                                        \______/                                   ''')
    
    print('-'*80)
    print("369 게임 시작~")
    print("박수를 쳐야할 땐 '짝'을 입력해주세요!")

def rule_365(num):
    count = 0
    clap = ["3","6","9"]
    for digit in str(num):
        if digit in clap:
            count += 1   
    if count > 0:
        return "짝"*count
    else:
        return str(num)

def ranList(num):
    digitCount = 1
    ranList = [num, "짝"]
    if digitCount != len(str(num)):
        digitCount = len(str(num))
        ranList.append("짝"*digitCount)
    return ranList

def playGame(players):
    num = 1
    clap = ["3","6","9"]
    failedPlayers = []
    while True:
        for player in players :
            if player == players[0] :
                playerCall = input(f"{player.getName()} : ")
                if playerCall != rule_365(num):
                    failedPlayers.append(player)
                    return failedPlayers
                    break
            else:
                if num in clap :
                    playerCall = random.choice(ranList(num))
                else:
                    playerCall = str(num)
                #playerCall = rule_365(num+1)
                print(f"{player.getName()} : {playerCall}")
                if playerCall != rule_365(num):
                    failedPlayers.append(player)
                    return failedPlayers
                    break
            num=num+1
        else:
            continue
        break

p1 = Player("윤서", 4)
p2 = Player("컴터", 4)
p1.setSelect(True)
p2.setSelect(False)
players = [p1,p2]

def playing369(players) :
    gameStart()
    failedPlayers = playGame(players)
    return failedPlayers
