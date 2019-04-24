import pandas as pd

excel_file_name = "../crawling/naver_realtime_keyword_search/excel/RTKS_20190409_21h42m.xlsx"
df = pd.read_excel(excel_file_name)
#df.head(4) # 없어도 잘됨
print(df)