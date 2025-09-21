import streamlit as st

def measurement_inputs():
    st.header("Enter Your Body Measurements")
    height = st.number_input("Height (cm)", min_value=120, max_value=250)
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200)
    forearm = st.number_input("Forearm (cm)", min_value=15, max_value=50)
    chest = st.number_input("Chest (cm)", min_value=50, max_value=150)
    waist = st.number_input("Waist (cm)", min_value=40, max_value=120)
    hips = st.number_input("Hips (cm)", min_value=40, max_value=140)
    goal = st.selectbox("Goal", ["Body Type 1", "Body Type 2", "Body Type 3"])
    return {
        "height": height,
        "weight": weight,
        "forearm": forearm,
        "chest": chest,
        "waist": waist,
        "hips": hips,
        "goal": goal
    }
