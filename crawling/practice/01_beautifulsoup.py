import bs4
html_str = "<html><div></div></html>" #크롤링할 url
bsObj = bs4.BeautifulSoup(html_str, "html.parser")

print(type(bsObj))
print(bsObj)
print(bsObj.find('div'))