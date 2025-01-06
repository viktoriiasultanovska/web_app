import streamlit as st

dir(st)

user_choice_slider = st.slider("Amount", min_value=10, max_value=30)
if user_choice_slider == 30:
    st.info("You made the right choice!")

user_choice_radio = st.radio("Amount", options=[10, 20, 30])
if user_choice_radio == 30:
    st.info("You made the right choice!")
