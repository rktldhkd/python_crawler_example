'''
이미지 크롤링!!
1. 크롤링할 이미지의 "이미지 주소 복사"
2. url-이미지주소, filename-서버에 저장할 이미지파일명
'''

'''구글에서 이미지 크롤링
구글 이미지 검색은 이미지마다 UUID 발급. url에 그 아이디에 맞는 이미지를 제공하므로, UUID를
크롤링할 수 있어야하는데, 구글이미지 검색하는 메인 페이지에 이 값이 없다. 따라서 구글에서
이미지 검색 시, 작게 보이는 이미지들만 따올 수 있는 듯.
'''

import os
import urllib.request
import requests
import bs4
from time import localtime, strftime

#날짜시간대 별로 폴더를 만들어서 그 시간대에 크롤링한 이미지들 저장할 폴더 생성
#이미 폴더가 존재하면 생성 x
def make_folder(filename):
    if not(os.path.isdir(filename)):
        os.mkdir(filename)


### 크롤링 시작
keyword      = "쯔위" # 네이버는 query에 검색값을 넣을 수 있다.
created_time = strftime("%Y%m%d_%Hh%Mm%Ss") # 파일명에 사용할 시간
created_time_folder = strftime("%Y%m%d_%Hh") # 시간대별로 폴더 생성. 거기에 이미지 집어넣음

#지난 24시간동안 업로드된 해당 키워드의 사진들 url
url_prefix = "https://search.naver.com/search.naver?where=image&section=image&query="
url_suffix = "&res_fr=0&res_to=0&sm=tab_opt&face=0&color=0&ccl=0&nso=so%3Ar%2Cp%3A1d%2Ca%3Aall&datetype=1&startdate=&enddate=&start=1"
url        = url_prefix + keyword + url_suffix

filename = "../crawling_images/naver_crawled_imgs/" #크롤링할 이미지를 저장할 디렉토리까지만 설정. 이미지파일명은 keyword으로 붙일거임.

html       = requests.get(url)
bs_obj     = bs4.BeautifulSoup(html.content, "html.parser")

total_imgs = []

div_photowall = bs_obj.find("div", {"class":"photowall"})
imgs          = div_photowall.findAll("img") # 이미지파일 class가 _img인데 이걸로 검색하면 총 52장의 사진 중, 50장만 뽑힌다... 누락값이 있다

# #이미지 태그 크롤링
for img in imgs:
    img_url = img['data-source']
    img_alt = img['alt']
    record  = {"img_url":img_url, "img_alt":img_alt}
    #total_imgs.append(img_url) #리스트에 값추가
    total_imgs.append(record) # 리스트에 딕셔너리 추가.


imageIndex=1
filename = filename + created_time_folder +"/" #날짜시간대별로 이미지를 저장할 폴더 생성 위함
make_folder(filename)#폴더 생성
for  image in total_imgs:
    image_url       = image['img_url']
    image_fileName  = created_time + "_" + keyword + str(imageIndex)
    image_extension = '.gif'
    #print(filename)

    full_fileName  = filename + image_fileName + image_extension # 문자+정수가 안되므로 정수를 String 변환
    urllib.request.urlretrieve(image_url, full_fileName)#이미지 저장

    imageIndex += 1


