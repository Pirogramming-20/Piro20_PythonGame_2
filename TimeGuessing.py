from Player.Player import Player
import random
import time

def printSelectPlayer(players):
    for player in players:
        if(player.isSelected()):
            print(f"{player.getName()} 님이 게임을 선택하셨습니다! 😍")

def printGameIntro():
    print("*"*100)
    print("시간 맞추기 게임!")
    print(" _____ _                  _____                     _               _____                      ")
    print("|_   _(_)                |  __ \                   (_)             |  __ \                     ") 
    print("  | |  _ _ __ ___   ___  | |  \/_   _  ___  ___ ___ _ _ __   __ _  | |  \/ __ _ _ __ ___   ___ ")
    print("  | | | | '_ ` _ \ / _ \ | | __| | | |/ _ \/ __/ __| | '_ \ / _` | | | __ / _` | '_ ` _ \ / _ \\")
    print("  | | | | | | | | |  __/ | |_\ \ |_| |  __/\__ \__ \ | | | | (_| | | |_\ \ (_| | | | | | |  __/")
    print("  \_/ |_|_| |_| |_|\___|  \____/\__,_|\___||___/___/_|_| |_|\__, |  \____/\__,_|_| |_| |_|\___|")
    print("                                                             __/ |                             ")
    print("                                                            |___/                              ")
    print("")
    print("*"*100)
    print("게임 규칙")
    print("")
    print("1분을 정확하게 맞춰보세요.")
    print("시작하면 처음 5초를 보여드린 이후 시간이 가려집니다.")
    print("*"*100)

def startGame(players):
    print("게임 시작!")
    
    start = time.time()
    for i in range(1,6):
        time.sleep(1)
        print(f"00:0{i}")
    
    input("1분이 된 것 같을 때 엔터를 눌러주세요.: ")
    end = time.time()
    difference = end - start
    return difference

def showResult(difference, players):
    playerResult = round(abs(difference - 60), 4)
    randomResult = [round(random.uniform(0.0, 2.0),4) for i in range(3)]
    resultList = []
    for player in players:
        if(player.isSelected()):
            resultList.append([player, playerResult])
        else:
            resultList.append([player, randomResult[0]])
            randomResult.pop(0)
    resultList = sorted(resultList, key=lambda x:x[1])

    print("*"*100)
    print("결과")
    print("*"*100)
    print(f"{'이름':10} {'결과 (초)':10}")
    for result in resultList:
        print(f"{result[0].getName():10} {result[1]:10}")
    return resultList

def deleteHeart(resultList):
    buttomResult = []
    buttomResult.append(resultList[-1][0])
    buttomTime = resultList[-1][1]
    for target in resultList[:-1]:
        if(target[1] == buttomTime):
            buttomResult.append(target[0])
    for buttom in buttomResult:
        print(f"아 누가누가 술을 마셔 {buttom.getName()}(이)가 술을 마셔 원~~샷🍺🍺🍺")
        buttom.subtractHeart()
    return buttomResult

def printPlayerState(players, buttomList):
    print("*"*100)
    for buttom in buttomList:
        for player in players:
            if(buttom.getName() == player.getName()):
                print(f"{player.getName()}은(는) 지금까지 1🍺! 치사량까지 {player.getHeart()}")
            else:
                print(f"{player.getName()}은(는) 지금까지 0🍺! 치사량까지 {player.getHeart()}")

def timeGuessingGame(players):
    printSelectPlayer(players)
    printGameIntro()
    isStart = input("준비되셨다면 1을 입력해주세요❤️: ")
    if(isStart == '1'):
        difference = startGame(players)
    resultList = showResult(difference, players)
    buttomList = deleteHeart(resultList)
    printPlayerState(players, buttomList)