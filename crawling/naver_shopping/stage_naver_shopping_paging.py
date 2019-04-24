import requests
from libs.naver_shopping.parser import parse
import json

#crawler : url에서 문자열(내용) 뽑아오기
#parser : 크롤링하는 비즈니스로직 py파일
#crawl 함수는 crawler.py 파일에꺼 수정해서 써도 되지만, 그냥 여기에서 다시 정의해서 씀.
#json 파일로 내보내기 시, 이 파일의맨 밑에 코드 2줄 사용.
#엑셀파일로 내보내기 시, analyze.py 의 비즈니스로직 사용 - 그냥 이 파일에서 실행버튼만 누르면 됨.(json파일이 먼저 만들어져 있어야 함.)

def crawl(keyword, pageNo):
    url  = "https://search.shopping.naver.com/search/all.nhn?query={}&cat_id=&frm=NVSHATC&PagingIndex={}".format(keyword,pageNo)
    data = requests.get(url)
    print(data, url)
    return data.content

totalProducts    = [] #페이징하면서 얻은 모든 데이터들 누적할 변수
theNumberOfPages = 10 #검색할 페이지 총 개수
keyword          = "샤오미"
for pageNo in range(1, theNumberOfPages+1): #여러 페이지에서 크롤링해옴.
    pageString    = crawl(keyword, pageNo)
    products      = parse(pageString)
    totalProducts += products

print(totalProducts)
print(len(totalProducts))

#json파일로 내보내기
#file = open("./products_paging.json", "w+")
#file.write(json.dumps(totalProducts))