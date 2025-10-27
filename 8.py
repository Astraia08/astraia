import streamlit as st
st.set_page_config(page_title='芝士院🧀档案合集', page_icon="✒",layout='wide')

c1,c2=st.columns([1,2])
with c1:
    st.image('https://www.northcentralfoods.com/wp-content/uploads/2020/10/Swiss-Cheese.jpg', width=300)
with c2:
    st.title("芝士院🧀档案合集")
    st.text('忍忍吧 生活就是这样 酸甜苦辣咸鲜麻酥脆嫩滑绵爽软糯韧弹 只能自己咽')
tab1, tab2, tab3,tab4,tab5,tab6 = st.tabs(["学生 小鸡大厨🐣 数字档案", "南宁美食数据仪表🍲", "终极一班相册集📺","终极一班音乐播放器🎮","终极一班视频网站📀","KO ONE个人简历生成器✒"])

with tab1:
    import streamlit as st

    st.title('学生 小鸡大厨🐣 数字档案')
    st.header('🏷️基本档案')
    st.text('学生ID:23031310102')
    st.markdown('注册时间：:yellow[2023-10-01 08:30:17]|精神状态：🚫绝对机密')
    st.markdown('当前教室：:yellow[实训楼204]|安全等级：一般般')
    st.header('📊 技能矩阵')

    c1, c2, c3 = st.columns(3)
    c1.metric(label="c语言", value="65%", delta="2%")
    c2.metric(label="python", value="75%", delta="8%")
    c3.metric(label="java", value="85%", delta="15%")

    import pandas as pd 
    import streamlit as st
    data = {
        '任务':['学生数字档案','课程系统管理','数据图表展示'],
        '状态':['✅完成','⭕核验中','❎未完成'],
        '难度':['🟡⚪⚪⚪⚪','🟡🟡⚪⚪⚪','🟡🟡🟡⚪⚪'],
    }
    index = pd.Series(['2023-10-01', '2023-10-05', '2023-10-12'],name='日期')
    df = pd.DataFrame(data, index=index)

    st.subheader('📑任务日志')
    st.table(df)

    st.subheader('📑代码展示')
    str='''
    a=1
    b=2
    print(a+b)
    '''

    st.code(str, language=None)
    st.caption('这是python代码')
    st.code(str,language="python", line_numbers=True)


    st.markdown('：:yellow[>>SYSTEM MESSAGE:]下一个任务目标已解锁')
    st.markdown('：:yellow[>>TARGET:]课程管理系统')
    st.markdown('：:yellow[>>COUNTDOWN:]2023-10-01')

with tab2:
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


    

with tab3:
    st.header("终极一班相册集📺")
    import streamlit as st

    st.set_page_config(page_title='终极一班',page_icon='📺')


    images = [
        {
            'ur1':'https://frhj.tv/ko_one/images/top.jpg',
         'parm':' KO ONE !'
         },
        {
            'ur1':'https://occ-0-1001-1723.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABe5HjPOkduFoFEdu0EgawVPANlJP8tcEwJst36KsilwFAN-GKRe4alm0RL62yRJdlHMxLoqKEzsjnz3Juj7LucA4fqFQ.jpg?r=fa8',
         'parm': 'DONG !'
         },
        {
            'ur1': 'https://i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/3/3xhzoa4yjjwliu7.jpg',
         'parm': 'KO ONE2 !'
         },
         {
            'ur1': 'https://p1.ssl.qhmsg.com/t01bf3eda1e4f450db4.jpg',
         'parm': 'KO ONE3 !'
         },    
          {
            'ur1':   'https://img04.sogoucdn.com/app/a/200861/565e8711f71f9b694ff5856ab814739d#900x506',
         'parm':'QIUQIU'
         }  ]  
    if 'ind' not in st.session_state:
       st.session_state['ind'] = 0


    def nextImg():
        st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)
    
    st.image(images[st.session_state['ind']]['ur1'], caption=images[st.session_state['ind']]['parm'])

    c1,c2 = st.columns(2)

    def prevImg():
        st.session_state['ind'] = (st.session_state['ind'] - 1) % len(images)

    with c1:
        st.button('上一张',on_click=prevImg,use_container_width=True)

    with c2:
        st.button('下一张',on_click=nextImg,use_container_width=True)


    
with tab4:
    import streamlit as st
    st.set_page_config(page_title='终极一班', page_icon='🎮')

    st.title('终极一班音乐播放器🎮')
    st.text("使用streamlit制作的简单音乐播放器，支持切歌和基本播放控制")

    images = [{'url':'https://music.163.com/song/media/outer/url?id=25714107.mp3',
               'photo':'https://p2.music.126.net/H7yASAE00WD6oEOyTWZlwA==/109951167430279841.jpg?param=1800y1800',
               'songer':'歌手  曾沛慈',
               'time':'时长  3:19',
               'cover':'专辑封面',
               'name':'一个人想着一个人'
               },
              {'url':'https://music.163.com/song/media/outer/url?id=27713623.mp3',
               'photo': 'https://p1.music.126.net/Xa9mgdDWlZLGrZGtvrXo4A==/2277088581176156.jpg?param=1800y1800',
               'songer':'歌手  汪东城/曾沛慈',
               'time':'时长  2:45',
               'cover':'专辑封面',
                'name':'在你离开那一天'
               },
              {'url':'https://music.163.com/song/media/outer/url?id=26213227.mp3',
               'photo': 'https://p1.music.126.net/rpD1kZYj5pNjM_HOYGYRqA==/2338661232304510.jpg?param=1800y1800',
               'songer':'歌手  SpeXial',
               'time':'时长  3:26',
               'cover':'专辑封面',
                'name':'发飙'
               },
              {'url': 'https://music.163.com/song/media/outer/url?id=25714105.mp3',
               'photo': 'https://p1.music.126.net/7136kwDE1UvY6uh0VXQ01g==/109951167220899564.jpg?param=1800y1800',
               'songer':'歌手  文雨非',
               'time':'时长  3:19',
               'cover':'专辑封面',
                'name':'对我好一点'
               },
          
    ]

    if 'ind' not in st.session_state:
        st.session_state['ind']=0

    def nextImg():
        st.session_state['ind']=(st.session_state['ind']+1) % len(images)
    a1,a2=st.columns([1,2])
    with a1:
        st.image(images[st.session_state['ind']]['photo'],caption=images[st.session_state['ind']]['cover'])
    with a2:
        st.title(images[st.session_state['ind']]['name'])
        st.subheader(images[st.session_state['ind']]['songer'])
        st.text(images[st.session_state['ind']]['time'])
        st.audio(images[st.session_state['ind']]['url'])
            
    c1,c2=st.columns(2)

    def prevImg():
        st.session_state['ind']=(st.session_state['ind']-1) % len(images)


    with c1:
        st.button('⏮上一首',on_click=prevImg,use_container_width=True)
    with c2:
        st.button('下一首⏭',on_click=nextImg,use_container_width=True)


    
with tab5:
    st.header("终极一班视频网站📀")
    import streamlit as st
    st.set_page_config(page_title='终极一班', page_icon='📀')

    video_url=[{
        'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/78/20/1574422078/1574422078-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&trid=f923bfde0ef44490b8aee7ccbf03a39h&mid=0&deadline=1761302659&oi=771356656&gen=playurlv3&os=cosovbv&og=hw&nbs=1&uipk=5&upsig=037156c3eadd436002ccd99d1854c36c&uparams=e,platform,trid,mid,deadline,oi,gen,os,og,nbs,uipk&bvc=vod&nettype=0&bw=743656&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
        'title':'【终极一班2｜裘球】她就是传闻中不存在的学生会长',
        'episode':'🍰',
        'synopsis':'无音乐，不终极'
        },{
        'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/46/02/432480246/432480246-1-208.mp4?e=ig8euxZM2rNcNbhBnWdVhwdlhzUHhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&oi=771356656&uipk=5&gen=playurlv3&deadline=1761302602&platform=html5&nbs=1&trid=0c47c76deeea4734809ffa1fd0a1971h&os=cosovbv&og=cos&upsig=5f63b82292ee92f79c251d53a8a1a22a&uparams=e,mid,oi,uipk,gen,deadline,platform,nbs,trid,os,og&bvc=vod&nettype=0&bw=2876698&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
        'title':'【终极一班2 || 东婷】我努力忘记，可是爱情怎么喊停',
        'episode':'😚',
        'synopsis':'相遇的前提是时空错位，当时空BUG被修正，关于汪大东和雷婷的一切又都回到原点 在错误的时间遇见对的人，我永远为十八岁的东婷意难平 这是我最不愿意去重温的一部剧，从终极一班3之后就没有再回顾过，只是没想到这么多年过去东婷还是让我动容 每次看到最后三集就开始情绪低落'
        },{
        'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/67/91/32794149167/32794149167-1-192.mp4?e=ig8euxZM2rNcNbRj7zdVhwdlhWTahwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=39c7c507617b4c4a8bbecadd4fa9414h&os=cosovbv&mid=0&nbs=1&uipk=5&oi=771356656&gen=playurlv3&og=hw&deadline=1761303324&platform=html5&upsig=56dee3fe5d64d0e2d42027365db499ba&uparams=e,trid,os,mid,nbs,uipk,oi,gen,og,deadline,platform&bvc=vod&nettype=0&bw=1344282&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
        'title':'“我，就是终极一班！”终极一班3飙战力指数，打斗高燃合集',
        'episode':'👊',
        'synopsis':'谁能阻止得了少年武士赴死呢！他们听不到啊'
        }]

    if 'ind' not in st.session_state:
        st.session_state['ind']=0

    st.title(video_url[st.session_state['ind']]['title']+ video_url[st.session_state['ind']]['episode'] )
    st.video(video_url[st.session_state['ind']]['url'])
    st.text(video_url[st.session_state['ind']]['synopsis'])


    c1,c2,c3=st.columns(3)


    def play(arg):
        st.session_state['ind']=int(arg)
        
    for i in range(len(video_url)):
        st.button(f'第{i+1}集',use_container_width=True,on_click=play,args=([i]))


    

with tab6:
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
                s=s+ nengli +','
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
