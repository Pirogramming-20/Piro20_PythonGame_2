# 랜덤하게 1 ~ 10 중 하나 선택
import random
import requests
from bs4 import BeautifulSoup as bs
import re


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
    # print(page)
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
            # print(idiom)
            meaning = get_idiom_meaning(idiom["link"])
            # print(meaning)
            idiom.update({"meaning": meaning})
            print(idiom)
            return idiom
        except Exception as e:
            print(e)
            continue


def process():
    print("지금부터 사자성어 게임 시작입니다!")
    quiz = make_quiz()


if __name__ == "__main__":
    process()
