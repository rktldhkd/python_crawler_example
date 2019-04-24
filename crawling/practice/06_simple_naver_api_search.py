#naver_api_search 의 내용을 줄여놓은 코드

# alt + enter 치면 모듈 설치할 수있는 메뉴 뜬다
import requests
from urllib.parse import urlparse

client_id = "ojTTdMBujKC0jXnoMrWv"
client_secret = "DXyPWDMIpV"
keyword = "쯔위"
#url에 요청변수 start, display를 써서 화면에 표시할 데이터 수를 지정 가능
url     = "https://openapi.naver.com/v1/search/blog?query=" + keyword +"&start=1&display=20"# json 결과
result  = requests.get(urlparse(url).geturl(), headers={"X-Naver-Client-Id" : client_id,
                                                        "X-Naver-Client-Secret" : client_secret})
print(result.json())