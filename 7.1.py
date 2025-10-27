import streamlit as st
st.set_page_config(page_title='个人简历生成器', page_icon="✒",layout='wide')


st.title('KO ONE!👊个人简历生成器')


c1,c2=st.columns([1,2])

with c1:
    st.subheader('人物档案')
    name = st.text_input('姓名', autocomplete='name')
    
    position = st.text_input('武器', autocomplete='position')
    
    number = st.text_input('学号', autocomplete='number')
    
    email = st.text_input('班级', autocomplete='email')

    import streamlit as st
    from datetime import datetime, timedelta

    date = st.date_input('出生日期', value=None)

    st.write('性别')
    sex = st.radio(
        '性别',
        ['男', '女', '其他'],
        horizontal=True,
        label_visibility='hidden')
   
    st.write('异能特性☸')
    degresss = st.selectbox(
        '异能特性',
        ['金', '木', '水','火','土'],
        label_visibility='collapsed')
    
    options_1= st.multiselect(
        '能力✴',
        ['瞬间移动', '再生能力', '身体隐形','念力控制','物品鉴定','灵魂吞噬','空间传送'],
         max_selections=7)

    st.subheader("攻击🤜🤛")
    my_range = range(0,300)
    numbers1 = st.select_slider('攻击', options=my_range, value=0)

    st.subheader("防御🛡")
    my_range = range(0,300)
    numbers2 = st.select_slider('防御', options=my_range, value=0)

    st.subheader("速度👟")
    my_range = range(0,300)
    numbers3 = st.select_slider('速度', options=my_range, value=0)

    st.subheader("体力💪")
    my_range = range(0,300)
    numbers4 = st.select_slider('体力', options=my_range, value=0)

    st.subheader("战斗经验（年）")
    my_range = range(0,100)
    numbers5 = st.select_slider('战斗经验（年）', options=my_range, value=0)

    st.subheader("战力指数🔥")
    values = st.slider(
    '战力指数',
    0,100000,(10000,20000))
    
    st.introduction= st.text_area(label='个人简介：', placeholder='请简要介绍您的专业背景、职业目标和个人特点',height=200, max_chars=200)

    from datetime import datetime, time

    st.write("每日最佳联系时间段")
    w1 = st.time_input("时间1")

    import pandas as pd
    from io import StringIO

    uploaded_file = st.file_uploader('上传个人照片')
    if uploaded_file is not None:
        bytes_date=uploaded_file.getvalue()
    
    


with c2:
    audio_file = 'https://music.163.com/song/media/outer/url?id=26213227.mp3'
    st.audio(audio_file)
    st.title('简历实时预览')
    a1,a2,a3=st.columns(3)
    with a1:
        if uploaded_file is not None:
            bytes_date=uploaded_file.getvalue()
            st.image(bytes_date,caption='**个人照片**',width=250)
    with a2:
        st.write('**姓名：**', name)
        st.write('**武器：**', position)
        st.write('**学号：**', number)
        st.write('**班级：**', email)
        st.write('**出生日期：**', date)
    with a3:
        st.write('**性别**',sex)
        st.write('**异能特性**',degresss)
        
        s=''
        for nengli in options_1:
            s=s+nengli+','
        st.write('**能力**', s)
        
        st.write('**攻击**',numbers1 )
        st.write('**防御**',numbers2 )
        st.write('**速度**',numbers3 )
        st.write('**体力**',numbers4 )
        st.write('**战斗经验**',numbers5 )
        st.write('**战力指数**', values)
        st.write("**最佳联系时间:**", w1)
       
    st.title('**个人简介**')
    st.write(st.introduction)
         
    


