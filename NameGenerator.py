import requests
from bs4 import BeautifulSoup
import random

def nameGenerator():
    names = []
    weight = []
    url = "https://baby-name.kr/annalRanking/2008/"

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # nameList = soup.select('.ant-table-row > td > a')
        nameDivs = soup.select('td > a')
        populationDivs = soup.select('tr > td:nth-child(3)')
        for idx, name in enumerate(nameDivs):
            names.append(name.get_text())
            weight.append(int(populationDivs[idx].get_text().replace(',', '')))
    else:
        print(response.status_code)
    result= []

    while(len(result)<5):
        randomName = random.choices(names, weights = weight, k=1)[0]
        for name in result:        
            if(randomName == name):
                continue
        result.append(randomName)
    return result