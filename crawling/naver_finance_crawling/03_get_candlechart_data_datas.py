import requests
from bs4 import BeautifulSoup


def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    bsObj = BeautifulSoup(result.content, "html.parser")
    return bsObj


def get_candle_chart_data(company_code):
    bsObj = get_bs_obj(company_code)

    tbl_no_info = bsObj.find("table", {"class": "no_info"})

    td_first = tbl_no_info.find("td", {"class": "first"})
    close = td_first.find("span", {"class": "blind"}).text  # 종가

    tr = tbl_no_info.findAll("tr")[0]  # 첫번째 tr
    td = tr.findAll("td")[1]  # 두번째 td
    high = td.findAll("span", {"class": "blind"})[0].text  # 고가

    tr = tbl_no_info.findAll("tr")[1]  # 두번째 tr
    td_open = tr.find("td", {"class": "first"})  # td.first
    open = td_open.find("span", {"class": "blind"}).text  # 시가
    td_low = tr.findAll("td")[1]
    low = td_low.find("span", {"class": "blind"}).text  # 저가

    return {"종가": close, "고가": high, "시가": open, "저가": low}

#딕셔너리=자바의 map
dic_company_codes={
    "naver":"035420",
    "sk hynics":"000660",
    "LG Display":"034220",
    "한국전력":"015760"
}

for key, value in dic_company_codes.items():
    company_name = key
    company_code = value

    print("[[ {} ]]".format(company_name))
    print("{}\n".format(get_candle_chart_data(company_code)))