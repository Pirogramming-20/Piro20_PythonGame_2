from Player.Player import Player
import random

def gameStart():
    print('-'*80)
    print("  /$$$$$$   /$$$$$$   /$$$$$$                                                   ")
    print(" /$$__  $$ /$$__  $$ /$$__  $$                                                  ")
    print("|__/  \ $$| $$  \__/| $$  \ $$        /$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$ ")
    print("   /$$$$$/| $$$$$$$ |  $$$$$$$       /$$__  $$ |____  $$| $$_  $$_  $$ /$$__  $$")
    print("  |___  $$| $$__  $$ \____  $$      | $$  \ $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$")
    print(" /$$  \ $$| $$  \ $$ /$$  \ $$      | $$  | $$ /$$__  $$| $$ | $$ | $$| $$_____/")
    print("|  $$$$$$/|  $$$$$$/|  $$$$$$/      |  $$$$$$$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$")
    print(" \______/  \______/  \______/        \____  $$ \_______/|__/ |__/ |__/ \_______/")
    print("                                     /$$  \ $$                                  ")
    print("                                    |  $$$$$$/                                  ")
    print("                                     \______/                                   ")

    
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
            if player.isUser :
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

def playing369(players) :
    gameStart()
    failedPlayers = playGame(players)
    return failedPlayers
