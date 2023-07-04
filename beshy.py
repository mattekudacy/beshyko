import streamlit as st
import pyperclip

st.title('Malungkot ang beshy ko generator')

text = st.text_input('Enter text here')
split = text.split(' ')
join = '🤸🏻'.join(split)
st.write(join)

if st.button('Copy to clipboard'):
    pyperclip.copy(join)
    st.write("Text copied to clipboard!")