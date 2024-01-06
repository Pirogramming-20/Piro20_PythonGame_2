from Player.Player import Player
import random
import time
import sys

def printSelectPlayer(players):
    for player in players:
        if(player.isSelected()):
            print(f"{player.getName()} 님이 게임을 선택하셨습니다! 😍")

def printGameIntro():
    print("*"*15)
    print("시간 맞추기 게임!")
    print("*"*15)
    print("게임 규칙")
    print("")
    print("1분을 정확하게 맞춰보세요.")
    print("시작하면 처음 5초를 보여드린 이후 시간이 가려집니다.")
    print("*"*15)

def startGame(players):
    print("게임 시작!")
    
    start = time.time()
    for i in range(1,6):
        time.sleep(1)
        print(f"00:0{i}")
    
    input("1분이 된 것 같을 때 아무 키나 눌러주세요.: ")
    end = time.time()
    difference = end - start
    return difference

def showResult(difference, players):
    playerResult = round(abs(difference - 60), 4)
    randomResult = [round(random.uniform(0.0, 2.0),4) for i in range(3)]
    resultDict = {}
    for player in players:
        if(player.isSelected()):
            resultDict[player.getName()] = playerResult
        else:
            resultDict[player.getName()] = randomResult[0]
            randomResult.pop(0)
    resultDict = sorted(resultDict.items(), key=lambda x:x[1])
    print("*"*15)
    print("결과")
    print("*"*15)
    print(f"{'이름':10} {'결과 (초)':10}")
    for result in resultDict:
        print(f"{result[0]:10} {result[1]:10}")

def deleteHeart(players, resultDict):
    buttomResult = []
    buttomResult.append(resultDict.popitem())
    while(len(resultDict)!=0):
        targetResult = resultDict.popitem()
        if(buttomResult == targetResult):
            buttomResult.append(targetResult)
    for buttom in buttomResult:
        buttom.subtractHeart()

def printPlayerState(players):
    print("*"*15)
    for player in players:
        print(f"{player.getName()}은(는) 지금까지 {player.getHeart()}개! 치사량까지 {player.getHeart()}")

def timeGuessingGame(players):
    printSelectPlayer(players)
    printGameIntro()
    isStart = input("준비되셨다면 1을 입력해주세요❤️: ")
    if(isStart == '1'):
        difference = startGame(players)
    resultDict = showResult(difference, players)
    deleteHeart(players, resultDict)
    printPlayerState(players)

player1 = Player("Yeonu", 5)
player2 = Player("Jimin", 5)
players = [player1, player2]
player1.setSelect(True)
player2.setSelect(False)
timeGuessingGame(players)