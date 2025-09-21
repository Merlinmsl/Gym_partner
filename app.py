import streamlit as st
from frontend.form_inputs import measurement_inputs
from frontend.progress_chart import show_progress
from backend.hardcoded_plans import get_hardcoded_plan
from backend.data_storage import save_user_data, load_user_history

st.title("AI Fitness & Nutrition Tracker (No AI Demo)")
st.write("Enter your details to receive a schedule suggestion and track progress weekly!")

# Gather inputs
user_data = measurement_inputs()

if st.button("Get My Plan"):
    # Save the new data
    save_user_data(user_data)
    # Get a schedule suggestion (hardcoded for demo)
    suggested_plan = get_hardcoded_plan(user_data['goal'])
    st.success("Your Suggested Plan:")
    st.write(suggested_plan)
    st.info(
        "This is a demo using example schedules. AI planning will be integrated soon!")

# Show progress chart if any history exists
history = load_user_history()
if history:
    weight_history = [entry['weight'] for entry in history]
    show_progress(weight_history)
else:
    st.info("No progress data to show yet. Enter your details to start tracking!")
