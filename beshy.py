import streamlit as st
import pyautogui

st.title('Malungkot ang beshy ko generator')

text = st.text_input('Enter text here')
join = '🤸🏻'.join(text.split(' '))
st.write(join)

if st.button('Copy to clipboard'):
    pyautogui.write(join)
    pyautogui.hotkey('ctrl', 'c')
    st.write("Text copied to clipboard!")

