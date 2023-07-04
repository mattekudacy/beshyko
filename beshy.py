import streamlit as st
import clipboard

st.title('Malungkot ang beshy ko generator')

text = st.text_input('Enter text here')
join = '🤸🏻'.join(text.split(' '))
st.write(join)

if st.button('Copy to clipboard'):
    clipboard.copy(join)
    st.write("Text copied to clipboard!")