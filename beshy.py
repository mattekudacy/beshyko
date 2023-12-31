import streamlit as st

def main():
    st.title('🤸🏻MALUNGKOT🤸🏻ANG🤸🏻BESHY🤸🏻KO🤸🏻GENERATOR🤸🏻')
    text = st.text_input('Enter text here').upper()
    join = '🤸🏻'.join(text.split(' '))

    Path_with_newlines = '\n'.join([join[i:i+70] for i in range(0, len(join), 50)])
    print(Path_with_newlines)
    st.code('''{}'''.format(Path_with_newlines), language="python")
    st.markdown("Copy your text!")

if __name__ == "__main__":
    main()
