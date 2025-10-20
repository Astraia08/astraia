import streamlit as st

st.title("学生 08 数字档案")
st.header('基础信息📜')
st.markdown('**学生ID**:yellow[23031310108]')
st.markdown('**学校**   *****')
st.markdown('**班级**   23高本数管1班')
st.markdown('**当前教室**   实训楼204')


st.subheader('收入情况💰')
st.metric(label="当日收入", value="0", delta="-100")


st.header('今日技能📊')
c1, c2, c3 = st.columns(3)
c1.metric(label="Python Streamlit", value="32%", delta="+10%")
c2.metric(label="打游戏", value="0%", delta="-50%")
c3.metric(label="看小说", value="10%", delta="+15%")


st.header('任务日志🖥')
import pandas as pd
import streamlit as st
data = {
    '任务':['学生数字档案',' 课程管理系统', '数据图表展示'],
    '状态':['完成✅','加载中⭕','加载中⭕'],
}
index = pd.Series(['2025-10-20', '——','——'], name='日期')
df = pd.DataFrame(data, index=index)
st.subheader('今日')
st.table(df)

import streamlit as st
import time
st.subheader('Streamlit课程进度')
progress_text_1='当前进度{80}%'
my_bar=st.progress(80,text=progress_text_1)
time.sleep(0.5)

  
