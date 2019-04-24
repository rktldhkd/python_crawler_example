import pandas as pd

df = pd.read_json('./products_paging.json')
print(df.count()) #잘 불러오는지 확인

writer = pd.ExcelWriter("./products_paging.xlsx")
df.to_excel(writer, "sheet1")
writer.save()