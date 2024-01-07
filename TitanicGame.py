from Player.Player import Player
import random

def printStart():
    print('-'*50)
    print("""
 .oooooo..o  o8o              oooo         o8o                              ooooooooooooo  o8o      .                          o8o            
d8P'    `Y8  `"'              `888         `"'                              8'   888   `8  `"'    .o8                          `"'            
Y88bo.      oooo  ooo. .oo.    888  oooo  oooo  ooo. .oo.    .oooooooo           888      oooo  .o888oo  .oooo.   ooo. .oo.   oooo   .ooooo.  
 `"Y8888o.  `888  `888P"Y88b   888 .8P'   `888  `888P"Y88b  888' `88b            888      `888    888   `P  )88b  `888P"Y88b  `888  d88' `"Y8 
     `"Y88b  888   888   888   888888.     888   888   888  888   888            888       888    888    .oP"888   888   888   888  888       
oo     .d8P  888   888   888   888 `88b.   888   888   888  `88bod8P'            888       888    888 . d8(  888   888   888   888  888   .o8 
8""88888P'  o888o o888o o888o o888o o888o o888o o888o o888o `8oooooo.           o888o     o888o   "888" `Y888""8o o888o o888o o888o `Y8bod8P' 
                                                            d"     YD                                                                         
                                                            "Y88888P'                                                                                                                                                                                       
    """)
    print('-'*100)
    print("맥주잔 안에 담긴 위태위태한 소주잔")
    print("소주는 100cc 이상 넘어갈 수 없습니다!")
    print("TIP! : 40cc 부터는 항상 조심하세요!")
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
    while True:
        for player in players:
            if player.isSelected():
                while True:
                    print('-'*50)
                    print(f"{player.getName()} 차례입니다. 소주 몇 cc를 부을 건가요? ", end="")
                    cc=input()
                    if cc.isdigit() and 0<int(cc) and int(cc)<40:
                        soju_cc+=int(cc)
                        break
                    else:
                        print("소주는 1~39 사이 정수 만큼만 부을 수 있습니다!")
                break
                
        if soju_cc>=sinking_point:
            print(f"당신의 한 방울로 {soju_cc}가 되어 한계인 {sinking_point}를 넘어서 그만...(기우뚱) \n 꼬르ㄹ...\n  ㄹ...")
            break              
        print(f"현재 소주잔은 {soju_cc}가 채워졌습니다!")
        changeNextPlayer(players)
        
def deleteHeart(players):
    for player in players:
        if player.isSelected():    
            print(f"아 누가누가 술을 마셔 {player.getName()}(이)가 술을 마셔 원~~샷")
            player.subtractHeart()
            break
    changeNextPlayer(players)


def titanicStart(players):
    printStart()
    gameStart(players)
    deleteHeart(players)