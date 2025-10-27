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
    st.button('第' +str(i+1) + '集',use_container_width=True,on_click=play,args=([i]))

    



