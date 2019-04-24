#한국거래소 크롤링은 복잡한 방식인 것 같은데, 인터넷에 자료도 부족하고, 있더라도 최신화된게 아니라 크롤링이 되지않는다.
#따라서 다른 사람이 만들어 놓은 모듈을 사용한다.

from time import strftime
from libs.korea_exchange.crawling_krx_stock_entire import get_stock_entire_list_from_krx
import json, os
import pandas as pd
'''
def save_stock_list_as_excel(file_name, target_date=None)
def get_stock_list_from_krx(target_date=None)

두 함수 모두, target_date에 지정한 datetime 객체의 날짜에 해당하는 국내 증시 상장 종목 리스트를 가져오는 함수로,

target_date를 지정하지 않을 경우 해당 날짜로부터 가장 가까운 시점에 업데이트 된 상장 주식 목록을 가져온다.

get_stock_list_from_krx 함수는 한국거래소의 데이터 딕셔너리를 json 배열형태로 반환한다:

save_stock_list_as_excel 함수는 file_name 인자로 지정한 파일이름으로 다음과 같은 엑셀 csv 파일을 저장한다.
[출처] 파이썬으로 거래소에서 국내 증시 종목 정보 얻어오기 - alphaj_krxcrawler 패키지|작성자 알파J인베스트먼트
'''
#크롤러 기능 외, 부수적 기능을 하는 함수들.
def make_dir(dir_url):
    #print(dir_url)
    if not(os.path.isdir(dir_url)):
        os.mkdir(dir_url)

def make_json(result):
    json_folder_url = "./json/" + strftime("%Y%m") + "/"
    make_dir(json_folder_url)

    created_time = strftime("%Y%m%d_%Hh%Mm")  # 파일명에 사용할 시간
    json_file_name = "krexc_stock_list_" + created_time # 파일명
    json_url = json_folder_url + json_file_name + ".json" #파일 저장할 경로, 파일명까지의 경로

    file = open(json_url, "w+") #저장할 경로 지정. 경로에 파일명까지 추가해서 설정해야한다!
    file.write(json.dumps(result)) #json 생성
    return {"json_file_name":json_file_name, "json_url":json_url}

#xlsx 엑셀 저장
def make_excel(json_info):
    excel_folder_url = "./excel/" + strftime("%Y%m") + "/"
    make_dir(excel_folder_url)

    df     = pd.read_json(json_info['json_url'])
    created_time = strftime("%Y%m%d_%Hh%Mm")  # 파일명에 사용할 시간
    writer = pd.ExcelWriter(excel_folder_url + json_info['json_file_name'] + ".xlsx") #엑셀파일 경로+파일명 지정
    df.to_excel(writer, "sheet1") #excel파일 sheet명 = sheet1
    writer.save() #엑셀파일 저장.

#csv 엑셀 저장
def make_excel_csv(data, json_info):
    excel_folder_url = "./excel/" + strftime("%Y%m") + "/"
    make_dir(excel_folder_url)

    df = pd.DataFrame(result, columns=['종목코드', '종목명', '현재가', '대비', '등락률', '시가', '고가', '저가', '거래량', '거래대금', '시가총액', '시가총액비중', '상장주식수'])
    created_time = strftime("%Y%m%d_%Hh%Mm")  # 파일명에 사용할 시간

    #encoding=euc-kr 지정 안해주면 엑셀에서 열때 한글이 깨져보인다. utf-8로 지정해도 소용없다.
    df.to_csv(excel_folder_url + json_info['json_file_name'] + ".csv", encoding="euc-kr")


crawled_time = strftime("%Y%m%d %H:%M:%S")
print("{} - {}".format(crawled_time, "통계-주식-종목시세-전체종목"))

result = get_stock_entire_list_from_krx()

json_info = make_json(result)
make_excel_csv(result, json_info)