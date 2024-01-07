# 랜덤하게 1 ~ 10 중 하나 선택
import random
import requests
from bs4 import BeautifulSoup as bs
import re
from Player.Player import Player

#### Utils ####


def crawl(url):
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    return soup


def remove_hanja(text):
    return re.sub(r'\([^)]*\)', '', text)


#### Game ####
# 10 페이지 중 하나 선택, 그중에서 한 개의 사자성어 선택
def choose_idiom():
    page = random.randint(1, 10)
    url = f"https://100.daum.net/book/25/list?sort=vcnt&index=&page={page}"
    soup = crawl(url)

    # 선택한 페이지의 사자성어 목록
    page_result = soup.find_all('a', class_="link_register")

    # 그중에서 한개의 사자성어 선택 + 사자성어 뜻이 있는 페이지 링트 반환
    idx = random.randint(0, len(page_result)-1)
    idiom = page_result[idx]
    idiom_text = remove_hanja(idiom.text).strip()
    link = idiom["href"]
    url = f"https://100.daum.net{link}"

    return {"idiom": idiom_text, "link": url}


def get_idiom_meaning(url):
    soup = crawl(url)
    meaning = soup.find('p', class_=lambda x: x and 'desc_section' in x).text
    return meaning


def make_quiz():
    while True:
        try:
            idiom = choose_idiom()
            meaning = get_idiom_meaning(idiom["link"])
            idiom.update({"meaning": meaning})
            # print(f"힌트: {idiom['idiom']}")
            return idiom
        except Exception as e:
            print(e)
            continue


def check_answer(answer, quiz):
    if answer == quiz["idiom"]:
        return True
    else:
        return False


def print_start():
    print("""

 ______        __  __                                 ______                                   
/      |      /  |/  |                               /      \                                  
$$$$$$/   ____$$ |$$/   ______   _____  ____        /$$$$$$  | ______   _____  ____    ______  
  $$ |   /    $$ |/  | /      \ /     \/    \       $$ | _$$/ /      \ /     \/    \  /      \ 
  $$ |  /$$$$$$$ |$$ |/$$$$$$  |$$$$$$ $$$$  |      $$ |/    |$$$$$$  |$$$$$$ $$$$  |/$$$$$$  |
  $$ |  $$ |  $$ |$$ |$$ |  $$ |$$ | $$ | $$ |      $$ |$$$$ |/    $$ |$$ | $$ | $$ |$$    $$ |
 _$$ |_ $$ \__$$ |$$ |$$ \__$$ |$$ | $$ | $$ |      $$ \__$$ /$$$$$$$ |$$ | $$ | $$ |$$$$$$$$/ 
/ $$   |$$    $$ |$$ |$$    $$/ $$ | $$ | $$ |      $$    $$/$$    $$ |$$ | $$ | $$ |$$       |
$$$$$$/  $$$$$$$/ $$/  $$$$$$/  $$/  $$/  $$/        $$$$$$/  $$$$$$$/ $$/  $$/  $$/  $$$$$$$/ 

                                                                                                                   
""")
    print("📢 지금부터 사자성어 게임 시작입니다!")
    print("제시된 사자성어의 뜻을 듣고👂, 사자성어를 맞춰주세요!✍\n")


def pick_next_player(players, current_player) -> Player:
    new_list = [elem for i, elem in enumerate(
        players) if elem != current_player]
    random_element = random.choice(new_list)
    return random_element

### MAIN Game ###
def idiom_game(players) -> Player:
    print_start()
    flag = True  # 탈락자가 있는지 여부
    player = players[0]
    while flag:
        print(f"💬 현재 플레이어는 {player.getName()}님 입니다!\n")
        quiz = make_quiz()
        print(f"🤷 {quiz['meaning']}\n해당 뜻을 가진 사자성어는 무엇일까요? 🤔")
        # 답변을 입력 받음
        if player.isUser:  # 플레이어 == 유저
            answer = input()
        else:  # 플레이어 == 컴퓨터
            # 컴퓨터는 40% 확률로 정답을 맞춘다.
            if random.randint(1, 100) <= 50:
                answer = quiz["idiom"]
            else:
                answer = "저는 잘 모르겠어요😅"
        # 정답 확인
        print(f"\n🙋 {player.getName()}님이 입력하신 정답은: {answer} 입니다!\n")
        if check_answer(answer, quiz):
            print("🙆 정답입니다!\n\n")
            player = pick_next_player(players, player)
        else:
            print(f"🤦 오답입니다! 정답은 {quiz['idiom']}입니다! 이로써 {player.getName()}님은 탈락입니다\n\n")
            flag = False
            return [player]
