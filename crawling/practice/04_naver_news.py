from urllib.request import urlopen
import bs4

url = "https://news.naver.com"
html = urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")
hdline_news = bsObj.find("ul", {"class":"hdline_article_list"}) #헤드라인 뉴스 리스트 ul-li
#print(hdline_news)

hdline_lis = hdline_news.findAll("li")
#print(hdline_lis)

#for문 출력 - 바로 출력할때 좋음.
for li in hdline_lis:
    news = li.find("a", {"class":"lnk_hdline_article"})
    #print(news)
    print(news.text)

print("========================================")

#list에 바로 넣는 법. for문 출력법에서 for문을 뒤에 쓰고, 로직을 앞에쓰는 식.
#list형식으로 변수에 넣어서 다른곳에 넘기거나 작업할 때 좋음.
titles = [news.find("a", {"class":"lnk_hdline_article"}).text for news in hdline_lis]
print(titles)
i=0
for title in titles[1:2]: #5항목(0~4) 중, 2번째항목(인덱스1) 을 추출. 1이상 2미만
   if(title != ''): #헤드라인 뉴스가 5개인데, 내용도 없는 6번째 항목을 만들어서 찍는다. 그래서 if문으로 비었는지 검사
        i+=1
        print("today's headline news {} : {}".format(i, title))