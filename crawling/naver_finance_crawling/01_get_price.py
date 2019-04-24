import requests
from bs4 import BeautifulSoup

def get_bs_obj(company_code):
    url     = "https://finance.naver.com/item/main.nhn?code="+company_code
    result  = requests.get(url)
    bsObj   = BeautifulSoup(result.content, "html.parser")
    return bsObj

def get_price(company_code):
    bsObj    = get_bs_obj(company_code)
    no_today = bsObj.find("p", {"class": "no_today"})
    price = no_today.find("span", {"class": "blind"}).text
    return price

company_code = ["005930", "000660", "005680"]
for code in company_code:
    print(get_price(code))