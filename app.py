import streamlit as st
import random

# streamlit run .\app.py

# Initialize the random number and session state
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

st.title("숫자 맞추기 게임")
st.write("1부터 100 사이의 숫자를 맞춰보세요!")

# User input
user_guess = st.number_input("숫자를 입력하세요:", min_value=1, max_value=100, step=1)

# Check the guess
if st.button("제출"):
    st.session_state.attempts += 1
    if user_guess < st.session_state.random_number:
        st.write("더 큰 숫자입니다!")
    elif user_guess > st.session_state.random_number:
        st.write("더 작은 숫자입니다!")
    else:
        st.write(f"축하합니다! {st.session_state.attempts}번 만에 맞추셨습니다!")
        # Reset the game
        st.session_state.random_number = random.randint(1, 100)
        st.session_state.attempts = 0