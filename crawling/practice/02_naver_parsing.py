import urllib.request
import bs4

url  = "https://www.naver.com/"
html = urllib.request.urlopen(url) # 크롤링할 웹페이지 불러옴

bsObj = bs4.BeautifulSoup(html, "html.parser") #크롤링을 위해 beautifulsoup 라이브러리에 웹페이지 넘김

#print(html.read())
#print(bsObj) - 얘만 써도 html 잘 긁어오는듯

top_right = bsObj.find("div", {"class":"area_links"}) # 크롤링하는 부분
print(top_right)

print("====================================================================================================")

a_favorite = top_right.find("a", {"class":"al_favorite"}) # top_right로 범위한정 한 곳에서 다시 찾는 것.
print(a_favorite)
print("====================================================================================================")
print(a_favorite.text) #html 코드에서 textNode의 값을 가져옴.


