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

created_time = strftime("%Y%m%d_%Hh%Mm%Ss") # 파일명에 사용할 시간
created_time_folder = strftime("%Y%m%d_%Hh") # 시간대별로 폴더 생성. 거기에 이미지 집어넣음

#지난 24시간동안 업로드된 해당 키워드의 사진들 url
url    = "https://www.google.com/search?q=%EC%AF%94%EC%9C%84&tbm=isch&source=lnt&tbs=qdr:d&sa=X&ved=0ahUKEwilheuojsDhAhWLw7wKHdgPD5sQpwUIIA&biw=2048&bih=1048&dpr=1"
html   = requests.get(url)
bs_obj = bs4.BeautifulSoup(html.content, "html.parser")

#print(bs_obj)

#구글은 alt에 "'검색어'에 대한 이미지 검색결과" 라는 alt값만 있어서 alt값을 파일명에 사용 가능
filename = "../crawling_images/google_crawled_imgs/" #크롤링할 이미지를 저장할 디렉토르까지만 설정. 이미지파일명은 img태그의 alt속성으로 붙일거임.
total_imgs = []

tbl_img = bs_obj.find("table", {"class":"images_table"})
imgs    = tbl_img.findAll("img")

#이미지 태그 크롤링
for img in imgs:
    img_url = img['src']
    img_alt = img['alt']
    record  = {"img_url":img_url, "img_alt":img_alt}
    #total_imgs.append(img_url) #리스트에 값추가
    total_imgs.append(record) # 리스트에 딕셔너리 추가.

imageIndex = 1
filename = filename + created_time_folder +"/" #날짜시간대별 폴더 생성위함.
make_folder(filename)#폴더 생성
for  image in total_imgs:
    image_url       = image['img_url']
    image_fileName  = created_time + "_" + image['img_alt'].split(" ")[0].replace("에", "") + str(imageIndex)
    image_extension = '.gif'

    full_fileName  = filename + image_fileName + image_extension # 문자+정수가 안되므로 정수를 String 변환
    urllib.request.urlretrieve(image_url, full_fileName)

    imageIndex += 1