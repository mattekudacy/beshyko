import streamlit as st

st.title('Malungkot ang beshy ko generator')

text = st.text_input('Enter text here').upper()
join = '🤸🏻'.join(text.split(' '))
st.text_area('Generated Text', value=join, height=200, key='generated_text')