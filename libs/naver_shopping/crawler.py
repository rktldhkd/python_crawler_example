import requests

#crawler : url에서 문자열(내용) 뽑아오기

def crawl(keyword):
    url  = "https://search.shopping.naver.com/search/all.nhn?query=%EC%83%A4%EC%98%A4%EB%AF%B8&cat_id=&frm=NVSHATC"
    data = requests.get(url)
    print(data.status_code, "   ", url)
    return data.content
