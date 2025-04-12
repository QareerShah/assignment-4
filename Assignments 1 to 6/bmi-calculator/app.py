import streamlit as st

st.title("BMI Calculator")

# User input
weight = st.number_input("Enter your weight in (kg)", min_value=0.0)
height = st.number_input("Enter your height in (cm)", min_value=0.0)

# Only calculate if inputs are valid
if st.button("Calculate BMI"):
    if height == 0:
        st.error("Height cannot be 0.")
    else:
        final_height = height ** 2
        bmi = weight / (final_height / 10000)
        st.success(f"Your BMI is {bmi:.2f}")

        # BMI category result
        if bmi < 18.5:
            st.warning("You are underweight")
        elif 18.5 <= bmi < 24.9:
            st.info("You are normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight")
        else:
            st.error("You are obese")  
