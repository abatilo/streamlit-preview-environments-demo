import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
st.write(x, 'cubed is', x ** 3)
