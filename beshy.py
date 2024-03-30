import streamlit as st

def main():
    st.title('🤸🏻MALUNGKOT🤸🏻ANG🤸🏻BESHY🤸🏻KO🤸🏻GENERATOR🤸🏻')
    text = st.text_input('Enter text here').upper()
    if text:
        join = '🤸🏻'.join(text.split(' '))
    
        Path_with_newlines = '\n'.join([join[i:i+70] for i in range(0, len(join), 50)])
        st.markdown("Copy your text!")
        st.code('''{}'''.format(Path_with_newlines), language="python")

if __name__ == "__main__":
    main()
