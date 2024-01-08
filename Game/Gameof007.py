import time
import random
from Player import Player


def play007BbangGame(players):
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
    player_s= [player.getName() for player in players]
    loser = []
    def play_turn(player):
        nonlocal z_index
        print(f"{player}의 턴")
        print(z[z_index])
        z_index = (z_index + 1) % len(z)
    
    for i in players:
        if i.isUser:
            m_player=i.getName()
            
    random.shuffle(player_s)
    print('''      __                                              __            __ 
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
            time.sleep(1)
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
                or p_a[right_player_index] != 'yell'
                or any(p == 'yell' for i, p in enumerate(p_a) if i != left_player_index and i != right_player_index)
            ):

                print(f"{m_player}의 패배")
                for i in players:
                    if i.getName()==m_player:
                        loser.append(i)
                break
            if cnt==3:
                
                print(f'{m_player}의 승리')
                for i in players:
                    if i.getName()!=m_player:
                        loser.append(i)
                
                break

    return loser
 
        
                
                
                                    
            
            
if __name__ == "__main__":


    play_007_bbang_game(players)
