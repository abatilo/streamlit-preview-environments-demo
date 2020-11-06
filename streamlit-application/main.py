import streamlit as st

x = st.text_input('Enter a string')
st.write('Your string reversed is', x[::-1])
