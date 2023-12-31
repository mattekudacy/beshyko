# import streamlit as st

# st.title('🤸🏻Malungkot ang beshy ko generator🤸🏻')

# text = st.text_input('Enter text here').upper()
# join = '🤸🏻'.join(text.split(' '))
# st.text_area('Generated Text', value=join, height=200, key='generated_text')
# # create a button that will copy the text to clipboard
# if st.button('Copy to clipboard'):
#     st.write('Copied to clipboard!')
#     st.experimental_set_query_params(text=join)
import streamlit as st
def main():
    st.title("Copy Paste in streamlit")
    pathinput = st.text_input("Enter your Path:")
    #you can place your path instead
    Path = f'''{pathinput}'''
    st.code(Path, language="python")
    st.markdown("Now you get option to copy")
if __name__ == "__main__":main()