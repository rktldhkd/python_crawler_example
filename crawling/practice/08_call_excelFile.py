import pandas as pd

'''
CSV 확장자 경우 (Comma separated value)

df = pd.read_csv("csv파일 경로")
printf(df) # 출력이 잘되면 잘 불러와진 것.
'''


'''
xlsx 확장자 경우(엑셀파일 확장자, 쌩 엑셀파일)
xlrd 모듈이 설치되어있어야 작동이 된다.
엑셀 레코드안의 데이터길이가 너무 길면 ...으로 컬럼의 데이터가 생략되어서 나온다
'''
df = pd.read_excel("./products_paging.xlsx")
df.head(4)
print(df)