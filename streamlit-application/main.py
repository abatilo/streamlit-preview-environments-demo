import streamlit as st

x = st.text_input('HELLO JON')
st.write('Your string reversed is', x[::-1])
