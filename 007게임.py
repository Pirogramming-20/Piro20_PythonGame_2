from Player.player import Player
import time
import random

def play_007_bbang_game(players):
    z = ['0', '0', '7', '🔫']
    z_index = 0

    def play_turn(player):
        nonlocal z_index
        print(f"{player}의 턴")
        print(z[z_index])
        z_index = (z_index + 1) % len(z)
    random.shuffle(players)
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
    print('순서와 자리 배치는',players)
    print(players[0],'부터 시작!')
    current_player_index = 0
    cnt=0
    while True:
        current_player = players[current_player_index]
        play_turn(current_player)
        
        # 플레이어 1은 키보드 입력으로 선택, 나머지는 랜덤으로 선택
        if current_player== '가':
            while True:
                selected_player_name = input(f'{current_player}님, 누구를 선택하시겠습니까? (플레이어 이름): ')
                if selected_player_name in players:
                    current_player_index = players.index(selected_player_name)
                    break
                else:
                    print("잘못된 플레이어 이름입니다. 다시 선택해주세요.")
        else:
            time.sleep(1)  # 잠시 대기
            selected_player_index = random.choice([i for i in range(len(players)) if i != current_player_index])
            print(f'{current_player}님이 {players[selected_player_index]}님을 선택했습니다.')
            current_player_index = selected_player_index
        
        # 빵이 나왔을 때 각 플레이어가 자기가 가만히 있을지, 아니면 으악을 할지를 랜덤하게 선택
        if z[z_index-1] == '🔫':
            cnt += 1
            p_a=[]
            left_player_index = (current_player_index - 1) % len(players)
            right_player_index = (current_player_index + 1) % len(players)
            for i, player in enumerate(players):
                if player == '가':
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
                or p_a[right_player_index] != 'yell' or p_a[current_player_index]!='quiet' or p_a[(current_player_index+2)%len(players)]!='quiet'
            ):
                print(" 가의 패배")
                
            #마찬가지로 플레이어 네임
                break
            if cnt==2:
                print('가의 승리')
                break
 

            
            
if __name__ == "__main__":
    player1 = Player("가", 3)
    player2 = Player("나", 3)
    player3 = Player("다", 3)
    player4 = Player("라", 3)
    
    players=[player1,player2,player3,player4]
    players= [player.getName() for player in players]
    
    # 게임 실행
    play_007_bbang_game(players)
