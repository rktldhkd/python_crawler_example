import requests
import bs4
import pandas as pd
import os
import json
from time import strftime
from com import mod_Interval as si # setInterval 정의한 py파일
import time, threading


StartTime=time.time() #setInterval을 위한 시작값. 현재시간


#크롤러 기능 외, 부수적 기능을 하는 함수들.
def make_dir(dir_url):
    if not(os.path.isdir(dir_url)):
        os.mkdir(dir_url)

def make_json(json_folder_url, result):
    created_time = strftime("%Y%m%d_%Hh%Mm")  # 파일명에 사용할 시간
    json_file_name = "RTKS_" + created_time # 파일명
    json_url = json_folder_url + json_file_name + ".json"

    file = open(json_url, "w+") #저장할 경로 지정. 경로에 파일명까지 추가해서 설정해야한다!
    file.write(json.dumps(result)) #json 생성
    return {"json_file_name":json_file_name, "json_url":json_url}

def make_excel(json_info):
    df     = pd.read_json(json_info['json_url'])
    writer = pd.ExcelWriter("./excel/" + json_info['json_file_name'] + ".xlsx") #엑셀파일 경로+파일명 지정
    df.to_excel(writer, "sheet1") #excel파일 sheet명 = sheet1
    writer.save() #엑셀파일 저장.


def crawling():
    #interval 돌 때 분기점을 알려주기위한 로그
    print('{}번째'.format(int((time.time() - StartTime)/10 )))
    
    #크롤러 본문 시작
    url  = "https://www.naver.com/"
    html = requests.get(url)

    #print(html.text)
    #RTKS = realtime keyword search
    bsObj = bs4.BeautifulSoup(html.text, "html.parser")
    div_RTKS = bsObj.find("div", {"class":"PM_CL_realtimeKeyword_rolling"})
    RTKS_wrapper = div_RTKS.findAll("span", {"class":"ah_k"}) # 실시간검색어 20위까지

    json_folder_url = "./json/"
    make_dir(json_folder_url)

    result = []
    item_index = 1
    for item in RTKS_wrapper:
        search_keyword = item.text
        record = {"순위":item_index, "검색어":search_keyword}
        result.append(record)
        item_index+=1


    json_info = make_json(json_folder_url, result) # json파일을 생성. 그 후 excel파일을 만들 때 필요한 json 파일의 정보들(경로/파일명)을 리턴
    make_excel(json_info) # excel파일 생성.


# start action every 0.6s
# setInterval 첫 번째 인자 : interval의 텀을 설정.
# setInterval 두 번째 인자 : 비즈니스로직 정의한 함수의 이름부분만 넘기면 된다.
# json, excel 파일은 interval timer가 다 끝나면 한꺼번에 만들어 진다...
#inter=setInterval(0.6,action)
inter=si.setInterval(10, crawling)
print('just after setInterval -> time : {:.1f}s'.format(time.time()-StartTime))
print("{} - 실시간 검색어 데이터 크롤링\n".format(time.time()))

# will stop interval in 5s
# t변수 선언/정의, start()부분 지우면 interval만 계속 돈다
t=threading.Timer(60,inter.cancel) #timer. 지정한 초 후 interval 종료

t.start()