import streamlit as st

starting_point = st.text_input('HELLO KELLY CONGRATS ON GETTING MARRIED', value='20000')
interest = st.slider('What is your interest rate percentage?', min_value=1, max_value=20, value=12)
years = st.slider('How many years are you waiting?', min_value=1, value=45)

def compound(P, r, t):
  return f'{(int(P) * (1 + (float(r) / 100.0)) ** float(t)):,.2f}'

st.write('If you start with $', starting_point, 'and you wait', years, 'years, you\'ll have $', compound(starting_point, interest, years))
