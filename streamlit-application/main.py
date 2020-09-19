import streamlit as st

x = st.text_input('What is your name?')
st.write('Your name reversed is', x[::-1])
