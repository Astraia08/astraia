import pandas as pd

pd.set_option('display.unicode.east_asian_width',True)

penguin_df=pd.read_csv('penguins-Chinese.csv',encoding='gbk')

print(penguin_df.head())
