import requests
import csv
import calendar
import datetime
from datetime import timedelta

def get_stock_entire_list_from_krx(target_date=None):
    otp_url = "http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx"
    s = requests.Session()

    if target_date is not None:
        today = target_date
    else:
        today = datetime.datetime.today()

    #여기서 주의깊게 봐야한다. 하나라도 누락되면, 밑의 down_res= s.post() 부분에서 데이터가 하나도 안뽑힌다.
    otp_data = {
        "name": "fileDown",
        "filetype": "csv",
        "url": "MKD/13/1302/13020101/mkd13020101",
        "market_gubun" : "ALL",
        "sect_tp_cd": "ALL",
        "schdate": today.strftime('%Y%m%d'),
        "lang": "ko",
        "pagePath": "/contents/MKD/13/1302/13020101/MKD13020101.jsp"
    }

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome / 73.0 .3683.86 Safari / 537.36"
    }

    otp_res = s.get(otp_url, params=otp_data, headers=header)

    down_url = "http://file.krx.co.kr/download.jspx"

    down_params = {"code": otp_res.text}

    req_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome / 73.0 .3683.86 Safari / 537.36",
        "Referer": otp_url
    }

    down_res = s.post(down_url, data=down_params, headers=req_header)

    decoded_content = down_res.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')

    my_list = list(cr)

    result = []

    #리스트 인덱스 탐색 시, 음수를 넣으면 끝에서 부터 탐색. -1을 넣으면 맨 끝 인덱스
    for row in my_list:
        result.append({
            '종목코드': row[1],
            '종목명': row[2],
            '현재가': row[3],
            '시가대비': row[4],
            '등락률': row[5],
            '시가': row[6],
            '고가': row[7],
            '저가': row[8],
            '거래량': row[9],
            '거래대금': row[10],
            '시가총액': row[11],
            '시가총액비중': row[12],
            '상장주식수': row[13],

            # 'stock_code': row[1],
            # 'stock_name': row[2],
            # 'price_now': row[3],
            # 'price_compare': row[4],
            # 'price_increase_rate': row[5],
            # 'price_open': row[6],
            # 'price_high': row[7],
            # 'price_low': row[8],
            # 'trading_volume': row[9],
            # 'trading_value': row[10],
            # 'aggregate value of listed stock': row[11],
            # 'ratio_of_aggregate value': row[12],
            # 'amount_of_listed_stock': row[13],
        })

    del(result[0])
    return result
