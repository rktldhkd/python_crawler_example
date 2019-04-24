from selenium import webdriver
from bs4 import BeautifulSoup as bs

import time
import os, sys

###############################################드라이버 생성###########################################################

#exe 파일 생성법. 프롬프트에서 입력
#pyinstaller -F --add-binary "C:\dev\git\python\python_crawler_example\webDriver\chromedriver.exe";"." naver_login_auto.py

#frozen은 pyinstaller에 의해 생겨난 변수. 그냥 지정하면 됨.
if getattr(sys, 'frozen', False): #exe 파일을 실행했을 때,
    #exe 실행 시, 내부적으로 sys._MEIPASS 변수가 chromedriver를 찾는거라함..
    chromeDriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromeDriver_path)
else: #파이썬에서 직접 실행
    #Chrome()안에 크롬의 드라이버 경로 지정. 지정 안하면, 캍은 폴더내에 드라이버가 있는지 탐색한다.
    driver = webdriver.Chrome('C:\dev\git\python\python_crawler_example\webDriver\chromedriver.exe')

#위의 if문을 없애고 아래만 쓰면, 파이썬에서만 사용할 때의 코드가 됨...
#driver = webdriver.Chrome('C:\dev\git\python\python_crawler_example\webDriver\chromedriver.exe')

#################################################로직 시작#############################################################

#페이지 이동
driver.get('https://nid.naver.com/nidlogin.login')
driver.maximize_window()

'''
#id값으로 객체를 찾고, 값을 지정
send_keys 로 값 보내면, 캡챠창으로 이동.(로봇인지 아닌지, 문자입력하는 창) 이걸 우회해야한다.
execute_script() 로 캡챠창 우회.
driver.find_element_by_id('id').send_keys('rktldhkd') #전달할 id값
driver.find_element_by_id('pw').send_keys('goodperson1!') #전달할 pwd값
'''

###로그인
#입력전 0.5초씩 기다린다. 대형사이트는 너무 빠르게 다수의 로그인 시도 시, 트래픽 공격으로 인식할 수 있기 때문.
id = 'rktldhkd'
pw = 'goodperson1!'

#send_keys가 네이버에 막혀서 execute_script 사용.
#네이버의 자동화된 소프트웨어를 걸러내는 알고리즘을 우회할 수 있다.
driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
time.sleep(1)

#위에서 지정한 데이터 보냄. 크롬 개발자 도구에서 로그인 버튼을 찾고,
#개발자도구 소스보기 창에서 해당 버튼의 소스 우클릭 후, copy-copy XPath 를 선택 후, 파이썬 파일에 붙여넣기 한다.
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(5)

###페이지 이동
#카페 페이지 자체의 url
page_url = 'https://cafe.naver.com/krbleach'
#앵커태그(<a>) 로 게시판 이동 시 필요한 앵커태그의 href 값
#a_url = '/ArticleList.nhn?search.clubid=29677596&search.menuid=34&search.boardtype=L'
a_url = '/ArticleList.nhn?search.clubid=29677596&search.menuid=34&search.boardtype=L&search.questionTab=A&search.totalCount=122&search.page={}' #여러 페이지의 게시글목록 가져오기 위함.
theNumberOfPages = 3 #검색할 페이지 총 개수

for pageNo in range(1, theNumberOfPages+1): #여러 페이지에서 크롤링해옴.
    #페이지 이동
    time.sleep(0.6)

    print("+++ {} 페이지 시작".format(pageNo))

    pageing_url = a_url.format(pageNo)
    driver.get(page_url + pageing_url)

    driver.switch_to.frame('cafe_main') #beautifulsoup으로 크롤링 시, iframe 의 소스를 긁어올때 그냥은 안되고, driver.switch_to.frame('iframe name값') 를 사용.
    bsObj = bs(driver.page_source, 'html.parser') #driver.page_source : 웹페이지의 소스코드값.
    div_boardList = bsObj.findAll("div", {"class":"article-board"})[1]
    titles = div_boardList.findAll("a", {"class":"article"})

    for title in titles:
        print(title.text.strip()) #strip() 내부의 쓸데없는 공백 제거
    print()
#print(len(titles))
time.sleep(2)
driver.close() #창닫기