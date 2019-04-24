from urllib.request import urlopen
import bs4

url = "https://www.naver.com/"
html = urlopen(url)

bsObj = bs4.BeautifulSoup(html,"html.parser")

ul = bsObj.find("ul", {"class" : "an_l"})

#for문으로 find()사용하여 하나씩 뽑으면 대괄호로 안감싸지고 그냥 하나씩 출력
#findAll() 사용하여 출력 시, List형태러 return되며, [ , , , ...] 로 감싸져서 한 뭉텅이로 출력됨.
lis = ul.findAll("li")

print(lis)

for li in lis:
    a_tag = li.find("a")
    span  = a_tag.find("span", {"class":"an_txt"}) #클래스 속성으로 찾지 않으면, a > span형제들 중, 첫번째로 선언된 애들만 뽑혀짐.
    print(span.text)