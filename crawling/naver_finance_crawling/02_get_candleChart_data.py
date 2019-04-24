import requests
from bs4 import BeautifulSoup

def get_bs_obj(company_code):
    url     = "https://finance.naver.com/item/main.nhn?code="+company_code
    result  = requests.get(url)
    bsObj   = BeautifulSoup(result.content, "html.parser")
    return bsObj

def get_candle_chart_data(company_code):
    bsObj    = get_bs_obj(company_code)

    td_first = bsObj.find("td", {"class":"first"})
    close = td_first.find("span", {"class":"blind"}).text #종가

    tbl_no_info = bsObj.find("table", {"class":"no_info"})

    tr = tbl_no_info.findAll("tr")[0] #첫번째 tr
    td = tr.findAll("td")[1] #두번째 td
    high = td.findAll("span", {"class":"blind"})[0].text #고가

    tr      = tbl_no_info.findAll("tr")[1]  # 두번째 tr
    td_open = tr.find("td", {"class":"first"})  # td.first
    open    = td_open.find("span", {"class":"blind"}).text #시가
    td_low  = tr.findAll("td")[1]
    low     = td_low.find("span", {"class":"blind"}).text #저가
    print(low)
    
    return {"close":close, "high":high, "open":open, "low":low}

close = get_candle_chart_data("035420") #종가
print(close)