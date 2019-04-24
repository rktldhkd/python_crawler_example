# 리팩토링 : 자주 쓰일 것 같은 코드들을 함수로 정리하여 보기 좋게 만드는 것.

import requests
from bs4 import BeautifulSoup

#url을 넣어서 bs_obj를 return하는 function
def get_bs_obj(url):
    result  = requests.get(url)
    return BeautifulSoup(result.content, "html.parser")
    #print(result.content)

def get_price(company_code):
    url = "https://finance.naver.com/item/main.nhn?code="+company_code
    bsObj = get_bs_obj(url)
    no_today = bsObj.find("p", {"class": "no_today"})
    price = no_today.find("span", {"class": "blind"}).text
    return price

url   = "https://finance.naver.com/item/main.nhn?code=005930"
bsObj = get_bs_obj(url)

price_samsung = get_price("005930")
price_sk_hynix = get_price("000660")
print("samsung : ", price_samsung)
print("sk_hynix : ", price_sk_hynix)
