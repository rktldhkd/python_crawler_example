from libs.naver_shopping.crawler import crawl
from libs.naver_shopping.parser import parse
import json

pageString = crawl('')
products = parse(pageString)
print(len(products))

#json파일로 내보내기
##file = open("./products.json", "w+")
##file.write(json.dumps(products))