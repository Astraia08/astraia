import streamlit as st
st.title('南宁美食数据仪表🍲')

import streamlit as st
import pandas as pd
import numpy as np

restaurants_data = {
    "餐厅": ['顺兴川味馆', '廖哥土鲫鱼下饭菜', '每天鲜古早味','一点点','小汤总大碗饭'],
    "评分": [4.8, 4.2, 4.1, 4.0, 4.2],
    "人均消费(元)": [20, 35, 15, 18, 20],
    "latitude": [22.845473, 22.840397, 22.840213, 22.833227, 22.853962],
    "longitude": [108.232036, 108.245341, 108.246341, 108.219436, 108.222574]

}
st.map(pd.DataFrame(restaurants_data))

df = pd.DataFrame(restaurants_data)


st.header('餐厅评分⭐️')
st.bar_chart(df.set_index('餐厅'), y='评分')

st.header('餐厅价格💰')
st.line_chart(df.set_index('餐厅'), y='人均消费(元)')

data={"用餐时段": ["11", "12", "13",  "17","18",'19','20'],
      '顺兴川味馆':[ 30, 60, 54, 34, 45, 58, 28],
      '廖哥土鲫鱼下饭菜':[ 36, 71, 50, 35, 88, 65, 40],
      '每天鲜古早味':[ 17, 50, 32, 40, 55, 43, 20],
      '一点点':[ 22, 65, 45, 33, 36, 65, 60],
      '小汤总大碗饭':[ 17, 35, 44, 46, 70, 76, 28]
}
df=pd.DataFrame(data)
index = pd.Series([1, 2, 3, 4,5,6,7], name='序号')
df.index = index      
st.header('用餐时段人流量🥢')
st.area_chart(df, x='用餐时段')

import time
st.subheader('当前拥挤程度')
progress_text_1='80%拥挤'
my_bar=st.progress(80,text=progress_text_1)
time.sleep(0.5)

st.header("📊 今日营销额升降")
col1, col2, col3 , co14, co15= st.columns(5)
col1.metric("顺兴川味馆", "85%", "2%") 
col2.metric("一点点", "77%", "-1%")
col3.metric("廖哥土鲫鱼下饭菜", "48%", "-5%")
co14.metric("每天鲜古早味", "37%", "-10%")
co15.metric("小汤总", "58%","-10%")

