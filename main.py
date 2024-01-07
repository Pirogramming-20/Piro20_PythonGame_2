from Player.Player import Player
from TimeGuessing import timeGuessingGame
from idiom import idiom_game
from Game369 import playing369
import random

def showIntro():
    print("~"*120)
    print('''
    _       _        ____   U  ___ u  _   _     U  ___ u   _            ____      _      __  __  U _____ u 
U  /"\  u  |"|    U /"___|   \/"_ \/ |'| |'|     \/"_ \/  |"|        U /"___|uU  /"\  uU|' \/ '|u\| ___"|/ 
 \/ _ \/ U | | u  \| | u     | | | |/| |_| |\    | | | |U | | u      \| |  _ / \/ _ \/ \| |\/| |/ |  _|"   
 / ___ \  \| |/__  | |/__.-,_| |_| |U|  _  |u.-,_| |_| | \| |/__      | |_| |  / ___ \  | |  | |  | |___   
/_/   \_\  |_____|  \____|\_)-\___/  |_| |_|  \_)-\___/   |_____|      \____| /_/   \_\ |_|  |_|  |_____|  
 \\    >>  //  \\  _// \\      \\    //   \\       \\     //  \\       _)(|_   \\    >><<,-,,-.   <<   >>  
(__)  (__)(_")("_)(__)(__)    (__)  (_") ("_)     (__)   (_")("_)     (__)__) (__)  (__)(./  \.) (__) (__)
                                                                                                          
    ''')
    print("~"*120)
    print("٩(๑•̀ㅂ•́)و     안주 먹을🍖 시간이 ⏰ 없어요 ❌ 마시면서 배우는 술게임 🍺     ٩(๑•̀ㅂ•́)و".center(100))
    print("~"*120)

def showOutro():
    print("~"*100)
    print(f"{'다음에 술마시면 또 불러주세요~ 안녕!':^100}")
    print("~"*100)

def makePlayers():
    players = []
    nameList = ["우진", "윤서", "선민", "연우", "용현"]

    playerName = input("오늘 거하게 취해볼 당신의 이름은?: ")
    print(f"{'소주 기준 당신의 주량은?':~^80}")
    print(f"{'1. 소주 반병 (2잔)':100}")
    print(f"{'2. 소주 반병에서 한병 (4잔)':100}")
    print(f"{'3. 소주 한 벙에서 한병 반 (6장)':100}")
    print(f"{'4. 소주 한병 반에서 두병 (8잔)':100}")
    print(f"{'5. 소주 두병 이상 (10잔)':100}")
    print("~"*100)
    while(True):
        playerHeart = input("당신의 치사량(주량)은 얼마만큼인가요?(1~5을 선택해주세요): ")
        if (playerHeart == '1'
            or playerHeart == '2'
            or playerHeart == '3'
            or playerHeart == '4'
            or playerHeart == '5'):
            playerUser = Player(playerName, int(playerHeart)*2)
            playerUser.isUser = True
            players.append(playerUser)
            break
        else:
            print("잘못된 값을 입력하셨습니다. 1, 2, 3, 4, 5 중 하나를 입력해주세요.")
    
    while(True):
        visitorNum = input("함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!): ")
        if (visitorNum == '1'
            or visitorNum == '2'
            or visitorNum == '3'):
            for _ in range(int(visitorNum)):
                newNameIdx = random.randint(0, len(nameList)-1)
                newHeart = random.randint(1, 5)*2
                newPlayer = Player(nameList[newNameIdx], newHeart)
                players.append(newPlayer)
                nameList.pop(newNameIdx)
            break
        else:
            print("잘못된 값을 입력하셨습니다. 1, 2, 3 중 하나를 입력해주세요.")    
    return players

def showPlayers(players):
    for player in players:
        print(f"오늘 함께 취할 친구는 {player.getName()}입니다! (치사량 : {player.getHeart()})")
    print("~"*100)

def showPlayerState(players):
    print("~"*100)
    for player in players:
        print(f"{player.getName()}은(는) 지금까지 0🍺! 치사량까지 {player.getHeart()}")
    print("~"*100)

def showGameList():
    print(f"{'오늘의 Alcohol GAME':^100}")
    print(f"{'1. 007 게임':30}")
    print(f"{'2. 사자성어 게임':30}")
    print(f"{'3. 1분 맞추기 게임:30'}")
    print(f"{'4. 369 게임':30}")
    print(f"{'5. 타이타닉 게임':30}")
    print("~"*100)

def getGame(players):
    gameNum = 0
    currentPlayer = players.pop(0)
    if(currentPlayer.isUser == True):
        while(True):
            gameNumStr = input(f"{currentPlayer.getName()}(이)가 좋아하는 랜덤 게임~랜덤 게임~무슨게임?: ")
            if(gameNumStr == '1'
               or gameNumStr == '2'
               or gameNumStr == '3'
               or gameNumStr == '4'
               or gameNumStr == '5'):
                gameNum = int(gameNumStr)
                break
            else:
                print("잘못된 값을 입력하셨습니다. 1, 2, 3, 4, 5 중 하나를 입력해주세요.")
    else:
        gameNum = random.randint(1, 5)

    print(f"{currentPlayer.getName()} 님이 게임을 선택하셨습니다! 😃")
    print("")
    print("-"*100)

    # random.shuffle(players)
    players = players.append(currentPlayer)
    return gameNum

def deleteHeart(buttomList):
    for buttom in buttomList:
        print(f"아 누가누가 술을 마셔 {buttom.getName()}(이)가 술을 마셔 원~~샷🍺🍺🍺")
        buttom.subtractHeart()

def printPlayerState(players, buttomList):
    print("*"*100)
    for buttom in buttomList:
        for player in players:
            if(buttom.getName() == player.getName()):
                print(f"{player.getName()}은(는) 지금까지 1🍺! 치사량까지 {player.getHeart()}")
            else:
                print(f"{player.getName()}은(는) 지금까지 0🍺! 치사량까지 {player.getHeart()}")

def checkExit():
    runGame = input("술게임 진행중! 다른 사람의 턴입니다. 그만하고 싶으면 \"exit\"를, 계속하고 싶으면 아무키나 입력해 주세요!: ")
    if(runGame == "exit"):
        return True
    else:
        return False
    
def checkGameOver(players):
    for player in players:
        if(player.getHeart()<=0):
            return True
    return False

def showGameOver(players):
    print("-"*100)
    print('''

  ooooooo8      o      oooo     oooo ooooooooooo        ooooooo  ooooo  oooo ooooooooooo oooooooooo  
o888    88     888      8888o   888   888    88       o888   888o 888    88   888    88   888    888 
888    oooo   8  88     88 888o8 88   888ooo8         888     888  888  88    888ooo8     888oooo88  
888o    88   8oooo88    88  888  88   888    oo       888o   o888   88888     888    oo   888  88o   
 888ooo888 o88o  o888o o88o  8  o88o o888ooo8888        88ooo88      888     o888ooo8888 o888o  88o8 
                                                                                                     
    ''')
    print("-"*100)
    for player in players:
        if(player.getHeart()<=0):
            print(f"{player.getName()}이(가) 전사헸습니다...꿈나라에서는 편히 쉬시길..zzz")

def startGame():
    isExit = False
    players = makePlayers()
    currentPlayer = players[0]
    gameNum = 0
    showPlayers(players)
    showPlayerState(players)
    while(True):
        if(currentPlayer.isUser == True):
            showGameList()
            gameNum = getGame(players)
        else:
            showGameList()
            gameNum = getGame(players)
            isExit = checkExit()
            if(isExit):
                break
        if gameNum == 1:
            buttomList = timeGuessingGame(players)
        elif gameNum == 2:
            buttomList = idiom_game(players)
        elif gameNum == 3:
            buttomList = timeGuessingGame(players)
        elif gameNum == 4:
            buttomList = playing369(players)
        elif gameNum == 5:
            buttomList = timeGuessingGame(players)
        deleteHeart(buttomList)
        printPlayerState(players, buttomList)
        if(checkGameOver(players)):
            showGameOver(players)
            break
        currentPlayer = players[0]   

def main():
    showIntro()
    while(True):
        isStart = input("게임을 진행할까요? (y/n): ")
        if isStart == 'y':
            startGame()
            break
        elif isStart == 'n':
            break
        else:
            print("잘못된 값을 입력하셨습니다. y 또는 n으로 입력해주세요.")
    showOutro()

if __name__ == "__main__":
    main()
