import streamlit as st
st.title("AI Fitness & Nutrition Planner")
height = st.number_input("Height (cm)", min_value=120, max_value=250)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200)
forearm = st.number_input("Forearm (cm)", min_value=15, max_value=50)
# Add other fields as needed
goal = st.selectbox("Goal", ["Lose Fat", "Gain Muscle", "Get Fit"])
if st.button("Get Plan"):
    # Call Ollama backend here
