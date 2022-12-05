import streamlit as st
import time
import pandas as pd


st.title('階級チェックアプリ')
st.write('階級をチェックしどの階級の試合に出ればいいか示します。')

s = st.selectbox('性別を選択してください',('男性','女性'))
w = float(st.number_input('体重を入力してください（kg）'))


if s == '男性':
    if w <=60:
        st.write('60キログラム級')
        st.write('代表選手は高藤直寿')
    elif 60< w <=66:
        st.write('66キログラム級')
        st.write('代表選手は阿部一二三、丸山城四郎')
    elif 66< w <=73:
        st.write('73キログラム級')
        st.write('代表選手は大野将平')
    elif 73< w <=81:
        st.write('81キログラム級')
        st.write('代表選手は長瀬貴規')
    elif 81< w <=90:
        st.write('90キログラム級')
        st.write('代表選手は向翔一郎')
    elif 90< w <=100:
        st.write('100キログラム級')
        st.write('代表選手はウルフアロン')
    elif w >100:
        st.write('100キログラム超級')
        st.write('代表選手は原沢久喜、斉藤立')
elif s == '女性':
    if w <=48:
        st.write('48キログラム級')
        st.write('渡名喜風南、角田夏実')
    elif 48< w <=52:
        st.write('52キログラム級')
        st.write('阿部詩')
    elif 52< w <=57:
        st.write('57キログラム級')
        st.write('芳田司')
    elif 57< w <=63:
        st.write('63キログラム級')
        st.write('代表選手は田代未来')
    elif 63< w <=70:
        st.write('70キログラム級')
        st.write('代表選手は新井千鶴')
    elif 70< w <=78:
        st.write('78キログラム級')
        st.write('代表選手は濱田尚里')
    elif w >78:
        st.write('78キログラム超級')
        st.write('代表選手は素根輝')






 