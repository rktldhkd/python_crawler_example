from bs4 import BeautifulSoup

#parser : 크로울링한 문자열에서 데이터 뽑기

def parse(pageStrig):
    bsObj = BeautifulSoup(pageStrig, "html.parser")
    ul = bsObj.find("ul", {"class":"goods_list"})
    lis = ul.findAll("li", {"class":"_itemSection"})

    products = []
    for li in lis:
        product = getProductInfo(li)
        products.append(product)

    return products

def getProductInfo(li):
    img   = li.find("img", {"class":"_productLazyImg"})
    alt   = img['alt'] #해당태그의 속성에 접근
    price = li.find("span", {"class": "num"}).text
    a     = li.find("a", {"class":"tit"})
    link  = a['href']

    #가격에 천단위 콤마 제거
    return {"name":alt, "price":price.replace(',', ""), "link":link}