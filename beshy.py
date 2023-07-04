import streamlit as st
import clipboard
import threading

def copy_to_clipboard(text):
    clipboard.copy(text)

st.title('Malungkot ang beshy ko generator')

text = st.text_input('Enter text here')
join = '🤸🏻'.join(text.split(' '))
st.write(join)

if st.button('Copy to clipboard'):
    # Create a new thread to copy the text to clipboard
    thread = threading.Thread(target=copy_to_clipboard, args=(join,))
    thread.start()
    st.write("Text copied to clipboard!")
