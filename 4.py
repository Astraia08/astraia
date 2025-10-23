import streamlit as st

st.set_page_config(page_title='最终幻想7re', page_icon='🎮')

images = [{'url':'https://gamingbolt.com/wp-content/uploads/2023/09/Final-Fantasy-7-Rebirth_08.jpg',
           'parm':'Final Fantay VII'
           },
          {'url': 'https://cogconnected.com/wp-content/uploads/2024/01/final-fantasy-7-rebirth-sephiroth-1.jpg',
           'parm':'Sephiroth'
           },
          {'url': 'https://cdn.webshopapp.com/shops/105494/files/486248914/square-enix-final-fantasy-vii-remake-intergrade-re.jpg',
           'parm':'Cloud'
           },
          {'url': 'https://global-img.gamergen.com/final-fantasy-vii-rebirth-pc04_0001043245.jpg',
           'parm':'Aerith'
           },
          
]

if 'ind' not in st.session_state:
    st.session_state['ind']=0

def nextImg():
    st.session_state['ind']=(st.session_state['ind']+1) % len(images)

st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['parm'])
c1,c2=st.columns(2)

def prevImg():
    st.session_state['ind']=(st.session_state['ind']-1) % len(images)


with c1:
    st.button('上一张',on_click=prevImg)
with c2:
    st.button('下一张',on_click=nextImg)


         
         
         
         
