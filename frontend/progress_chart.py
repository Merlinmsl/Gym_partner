import streamlit as st

def show_progress(weight_history):
    st.subheader("Weight Progress Over Time")
    if weight_history:
        st.line_chart(weight_history)
    else:
        st.info("No progress data to show yet. Enter details to start tracking!")
