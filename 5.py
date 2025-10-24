import streamlit as st
st.set_page_config(page_title='终极一班', page_icon='🎮')

st.title('简易音乐播放器🎶')
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

