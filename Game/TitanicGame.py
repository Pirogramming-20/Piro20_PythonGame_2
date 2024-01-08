from Player import Player
import time
import random

def printStart():
    print('-'*100)
    print("""
  ______    _            __        _                    _________  _   _                    _          
.' ____ \  (_)          [  |  _   (_)                  |  _   _  |(_) / |_                 (_)         
| (___ \_| __   _ .--.   | | / ]  __   _ .--.   .--./) |_/ | | \_|__ `| |-',--.   _ .--.   __   .---.  
 _.____`. [  | [ `.-. |  | '' <  [  | [ `.-. | / /'`\;     | |   [  | | | `'_\ : [ `.-. | [  | / /'`\] 
| \____) | | |  | | | |  | |`\ \  | |  | | | | \ \._//    _| |_   | | | |,// | |, | | | |  | | | \__.  
 \______.'[___][___||__][__|  \_][___][___||__].',__`    |_____| [___]\__/\'-;__/[___||__][___]'.___.' 
                                              ( ( __))                                                                                                                                                                                     
    """)
    print('-'*100)
    print("찰랑거리는 맥주잔 속에 담겨진 위태로운 소주잔")
    print("소주는 100cc 이상 넘어갈 수 없습니다!")
    print("***TIP*** : 40cc부터는 항상 조심하세요!")
    return

def changeNextPlayer(players):
    for i in range(len(players)):
        if players[i].isSelected():
            players[i].setSelect(False)
            break
    if i==len(players)-1:
        players[0].setSelect(True)
    else:
        players[i+1].setSelect(True)
    

def gameStart(players):
    sinking_point=random.randint(40,100)
    soju_cc=0
    for i in range(len(players)):
        if i==0:
            players[i].setSelect(True)
        else:
            players[i].setSelect(False)
    while True:
        for player in players:
            if player.isSelected():
                if player.isUser:
                    while True:
                        print('-'*50)
                        cc=input(f"{player.getName()} 차례입니다. 소주 몇 cc를 부을 건가요? ")
                        if cc.isdigit() and 0<int(cc) and int(cc)<40:
                            soju_cc+=int(cc)
                            print(f"{player.getName()}(이)가 소주를 {int(cc)}만큼 붓습니다..")
                            time.sleep(1)
                            print(f"현재 소주잔은 {soju_cc}(이)가 채워졌습니다!")
                            break
                        else:
                            print("소주는 1~39 사이 정수 만큼만 부을 수 있습니다!")
                else:
                    print('-'*50)
                    if(soju_cc>=40):
                        num=random.randint(1,15)
                    else:
                        num=random.randint(10,35)
                    print(f"{player.getName()} 차례입니다. 소주 몇 cc를 부을 건가요? {num}")
                    soju_cc+=num
                    print(f"{player.getName()}(이)가 소주를 {num}만큼 붓습니다..")
                    time.sleep(1)
                    print(f"현재 소주잔은 {soju_cc}(이)가 채워졌습니다!")
            
        if soju_cc>=sinking_point:
            print(f"당신의 한 방울로 {soju_cc}cc가 되어 한계인 {sinking_point}cc에 도달해서 그만...(기우뚱) \n 꼬르ㄹ...\n  ㄹ...\n")
            break              
        changeNextPlayer(players)
        
def deleteHeart(players):
    sub_people=[]
    for player in players:
        if player.isSelected():    
            sub_people.append(player)
    return sub_people
    


def titanicGame(players):
    printStart()
    gameStart(players)
    return deleteHeart(players)