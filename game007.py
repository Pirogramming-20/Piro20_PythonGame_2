import time
import random
from Player.Player import Player

def play007BbangGame(players):
    player_s= [player.getName() for player in players]
    z = ['''
  ___  
 / _ \ 
( (_) )
 \___/ 
       ''', '''
  ___  
 / _ \ 
( (_) )
 \___/ 
       ''',
         '''
___ 
(__ )
 / / 
(_/
''', '🔫']
    z_index = 0

    losers = []
    print(player_s)
    def play_turn(player):
        nonlocal z_index
        print(f"{player}의 턴")
        print(z[z_index])
        z_index = (z_index + 1) % len(z)
    
    m_player=player_s[0]
    random.shuffle(player_s)
    print('''                   __                                              __            __ 
                  /  |                                            /  |          /  |
  _______        _$$ |_           ______          ______         _$$ |_         $$ |
 /       |      / $$   |         /      \        /      \       / $$   |        $$ |
/$$$$$$$/       $$$$$$/          $$$$$$  |      /$$$$$$  |      $$$$$$/         $$ |
$$      \         $$ | __        /    $$ |      $$ |  $$/         $$ | __       $$/ 
 $$$$$$  |        $$ |/  |      /$$$$$$$ |      $$ |              $$ |/  |       __ 
/     $$/         $$  $$/       $$    $$ |      $$ |              $$  $$/       /  |
$$$$$$$/           $$$$/         $$$$$$$/       $$/                $$$$/        $$/ 
                                                                                    
                                                                                    
                                                                                    
  ______          ______         ________              __                           
 /      \        /      \       /        |            /  |                          
/$$$$$$  |      /$$$$$$  |      $$$$$$$$/             $$ |                          
$$$  \$$ |      $$$  \$$ |          /$$/              $$ |                          
$$$$  $$ |      $$$$  $$ |         /$$/               $$ |                          
$$ $$ $$ |      $$ $$ $$ |        /$$/                $$/                           
$$ \$$$$ |      $$ \$$$$ |       /$$/                  __                           
$$   $$$/       $$   $$$/       /$$/                  /  |                          
 $$$$$$/         $$$$$$/        $$/                   $$/                           
                                                                                    
                                                                           ''')
    print('빰빠라바밤 빠바밤 빰바라밤바 빰빰바~🔫🔫🔫')
    print('순서와 자리 배치는',player_s)
    print(player_s[0],'부터 시작!')
    current_player_index = 0
    cnt=0
    while True:
        current_player = player_s[current_player_index]
        play_turn(current_player)
        
        # 플레이어 1은 키보드 입력으로 선택, 나머지는 랜덤으로 선택
        if current_player== m_player:
            while True:
                selected_player_name = input(f'{current_player}님, 누구를 선택하시겠습니까? (플레이어 이름): ')
                if selected_player_name in player_s:
                    current_player_index = player_s.index(selected_player_name)
                    break
                else:
                    print("잘못된 플레이어 이름입니다. 다시 선택해주세요.")
        else:
            time.sleep(1)  # 잠시 대기
            selected_player_index = random.choice([i for i in range(len(player_s)) if i != current_player_index])
            print(f'{current_player}님이 {player_s[selected_player_index]}님을 선택했습니다.')
            current_player_index = selected_player_index
        
        # 빵이 나왔을 때 각 플레이어가 자기가 가만히 있을지, 아니면 으악을 할지를 랜덤하게 선택
        if z[z_index-1] == '🔫':
            cnt += 1
            p_a=[]
            left_player_index = (current_player_index - 1) % len(player_s)
            right_player_index = (current_player_index + 1) % len(player_s)
            for i, player in enumerate(player_s):
                if player == m_player:
                    while True:
                        action = input('quiet / yell: ')
                        if action == 'quiet':
                            print(f"{player}님이 가만히 있습니다.")
                            p_a.append(action)
                            break
                        elif action == 'yell':
                            print(f"{player}님이 '으악'을 합니다.")
                            p_a.append(action)
                            break
                        else:
                            print('quiet / yell 중 하나를 선택하세요.')
                else:
                    if i==left_player_index or i==right_player_index:
                        action = 'yell'
                        print(f"{player}님이 '으악'을 합니다." )
                        p_a.append(action)
                    else:
                        action = 'quiet'
                        print(f"{player}님이 가만히 있습니다." )
                        p_a.append(action)

            if (
               p_a[left_player_index] != 'yell'
                or p_a[right_player_index] != 'yell' or p_a[current_player_index]!='quiet' or p_a[(current_player_index+2)%len(player_s)]!='quiet'
            ):
                print(f"{m_player}의 패배")
                for player in players:
                    if(player.getName()== m_player):
                        losers.append(player)
                
                break
            if cnt==2:
                
                print(f'{m_player}의 승리')
                losers = players.copy()
                for idx, player in enumerate(players):
                    if(player.getName()==m_player):
                        losers.pop(idx)
                
                break
    print(losers)   
    return losers
        
player1 = Player("연우", 2)
player2 = Player("철수", 3)
players = [player1, player2]
play007BbangGame(players)